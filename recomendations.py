import time
from sqlalchemy.orm import lazyload, subqueryload, joinedload, selectinload, noload
from main import MoviesDatabase, UsersFilms, db, UserSuggestion, Actors, Directors, Genres
import random


class MovieRecommendations:

    def __init__(self, user_id):
        self.points = 0
        self.highest_score = 0
        self.movie_to_recommend = None
        self.actors_dict = {}
        self.genres_dict = {}
        self.directors_dict = {}
        self.writers_dict = {}
        self.year_dict = {}
        self.PG_dict = {}
        self.users_id_list = [movie.movie_id for movie in UsersFilms.query.filter(UsersFilms.user_id == user_id).all()]
        self.user_id = user_id

    def prepare_score(self, movie, points):
        if movie.tag == 'heart':
            score = points * 2
        elif movie.tag == 'dislike':
            score = -(points * 2)
        elif movie.tag == 'bookmark':
            score = points
        elif movie.tag == 'ignore':
            score = -points
        return score

    def populate_dictionary(self, movie, column_name, dictionary_name, points):
        for item in column_name:

            if item.id in list(dictionary_name.keys()):
                dictionary_name[item.id] += self.prepare_score(movie, points)
            else:
                dictionary_name[item.id] = self.prepare_score(movie, points)

    def get_simple_dict(self, movie, item_def, dictionary_name, points):
        if item_def != '':
            if item_def in dictionary_name:
                dictionary_name[item_def] += self.prepare_score(movie, points)
            else:
                dictionary_name[item_def] = self.prepare_score(movie, points)

    def populate_all_dictionaries(self):
        for movie in UsersFilms.query.filter(UsersFilms.user_id == self.user_id). \
                filter(MoviesDatabase.id.in_(self.users_id_list)). \
                join(UsersFilms.movies_database). \
                options(joinedload(UsersFilms.movies_database)). \
                join(UsersFilms.users_actors). \
                options(joinedload(UsersFilms.users_actors)). \
                join(UsersFilms.users_genres). \
                options(joinedload(UsersFilms.users_genres)). \
                all():
            self.populate_dictionary(movie, movie.users_actors, self.actors_dict, 10)
            self.populate_dictionary(movie, movie.users_genres, self.genres_dict, 25)
            self.populate_dictionary(movie, movie.movies_database.director_of, self.directors_dict, 25)
            self.populate_dictionary(movie, movie.movies_database.writer_of, self.writers_dict, 10)
            self.get_simple_dict(movie, movie.movies_database.release_date[:4], self.year_dict, 10)
            self.get_simple_dict(movie, movie.movies_database.PG, self.PG_dict, 25)

    def clean_up_dictionaries(self):
        self.actors_dict = {}
        self.genres_dict = {}
        self.directors_dict = {}
        self.writers_dict = {}
        self.year_dict = {}
        self.PG_dict = {}
        self.users_id_list = []

    def add_points(self, table_name, dict_name):
        for item in table_name:
            if item.id in dict_name.keys():
                self.points += dict_name[item.id]

    def get_liked_items(self, dictionary):
        liked_items = []
        for key in dictionary:
            if dictionary[key] > 0:
                liked_items.append(key)
        return liked_items

    def give_points_for_score(self, movie):
        if movie.computed_critic_score:
            self.points += movie.computed_critic_score

        if movie.computed_audience_score:
            self.points += movie.computed_audience_score

    def split_the_points(self, movie):
        self.points = 0

        self.add_points(movie.actors, self.actors_dict)
        self.add_points(movie.genres, self.genres_dict)
        self.add_points(movie.director_of, self.directors_dict)
        self.add_points(movie.writer_of, self.writers_dict)

        if int(movie.release_date[:4]) - 1 in self.year_dict.keys():
            self.points += self.year_dict[movie.release_date[:4]]
        elif int(movie.release_date[:4]) in self.year_dict.keys():
            self.points += self.year_dict[movie.release_date[:4]]
        elif int(movie.release_date[:4]) + 1 in self.year_dict.keys():
            self.points += self.year_dict[movie.release_date[:4]]

        if movie.PG in self.PG_dict.keys():
            self.points += self.PG_dict[movie.PG]

        self.give_points_for_score(movie)

    def update_recommendations(self):
        self.populate_all_dictionaries()
        for movie in MoviesDatabase.query. \
                filter(Actors.id.in_(self.get_liked_items(self.actors_dict))). \
                filter(MoviesDatabase.computed_critic_score > 70). \
                filter(MoviesDatabase.id.notin_(self.users_id_list)). \
                join(MoviesDatabase.actors). \
                options(joinedload(MoviesDatabase.actors)). \
                join(MoviesDatabase.genres). \
                options(joinedload(MoviesDatabase.genres)). \
                join(MoviesDatabase.director_of). \
                options(joinedload(MoviesDatabase.director_of)). \
                all():

            self.split_the_points(movie)

            if self.points > self.highest_score:
                self.highest_score = self.points
                self.movie_to_recommend = movie.id
        return self.movie_to_recommend

    def get_good_movie(self):
        movie = MoviesDatabase.query.filter(MoviesDatabase.computed_critic_score > 85). \
            filter(MoviesDatabase.computed_audience_score > 85).filter(MoviesDatabase.id.notin_(self.users_id_list)).first().id
        return movie


