import itertools
import json
import math
import re
from collections import Counter
import sqlalchemy
from sqlalchemy import and_, func
from main import MoviesDatabase, UsersFilms, db, UserSuggestion, Actors


class MovieRecommendations:

    def __init__(self):
        self.points = 0
        self.suggestions = UserSuggestion.query
        self.movie_base = MoviesDatabase.query
        self.users_films = UsersFilms.query
        self.clear_old_recommendations()

    def clear_old_recommendations(self):
        self.suggestions.delete()
        db.session.commit()

    def give_points(self, list_name, points, movie_type):
        for item in list_name:
            if str(item) in movie_type:
                self.points += points

    def give_points_for_score(self, movie):
        if movie.computed_critic_score:
            self.points += movie.computed_critic_score * 2

        if movie.computed_audience_score:
            self.points += movie.computed_audience_score * 2

    def update_recommendations(self, user_id):
        print(self.users_films.filter_by(user_id=user_id).all())

        for movie in self.movie_base.filter(MoviesDatabase.computed_critic_score > 70) \
                             .filter(MoviesDatabase.id.notin_(movie.movie_id for movie in self.users_films.filter_by(user_id=user_id).all())) \
                             .order_by(func.random()).all():
            print(movie.id)

            self.points = 0

            self.give_points_for_score(movie)

            new_movie = UserSuggestion(points=self.points, title=movie.title, computed_critic_score=movie.
                                       computed_critic_score, computed_audience_score=movie.computed_audience_score)
            db.session.add(new_movie)

        db.session.commit()


recommend = MovieRecommendations()
recommend.update_recommendations(2)
