from flask import request, session
from sqlalchemy import or_, cast, Integer

from main import MoviesDatabase


class MoviebaseFilters:
    def __init__(self):
        self.search = request.args.get('search')
        self.index = int(request.args.get('index'))
        self.order = request.args.get('order')

        self.genres = request.args.get('genres').split(',')
        self.rating = request.args.get('rating')
        self.critics = request.args.get('critics')
        self.audience = request.args.get('audience')

        self.key = request.args.get('key')
        self.movies = MoviesDatabase.query


    # def find_key(self):
    #     try:
    #         searched_data = session['searched_data']
    #         session['searched_data'] = ''
    #         self.key = searched_data
    #     except KeyError:
    #         self.key = request.args.get('key')
    #     return self.key

    def search_by(self):
        search_by = {'title': MoviesDatabase.title,
                     'collection': MoviesDatabase.collection,
                     'director': MoviesDatabase.director,
                     'cast': MoviesDatabase.cast,
                     'studio': MoviesDatabase.studio}

        self.movies = self.movies.filter(or_(
            search_by[self.search].startswith(self.key),
            search_by[self.search].contains(f' {self.key}')))

    def order_by(self):
        order_by = \
            {'critics_max': self.movies.filter(MoviesDatabase.tomatometer != '').order_by(
                cast(MoviesDatabase.computed_critic_score, Integer).desc()),
                'critics_min': self.movies.filter(MoviesDatabase.tomatometer != '').order_by(
                    cast(MoviesDatabase.computed_critic_score, Integer)),
                'boxoffice_max': self.movies.filter(MoviesDatabase.boxoffice != '0').order_by(
                    cast(MoviesDatabase.boxoffice, Integer).desc()),
                'boxoffice_min': self.movies.filter(MoviesDatabase.boxoffice != '0').order_by(
                    cast(MoviesDatabase.boxoffice, Integer)),
                'date_max': self.movies.order_by(MoviesDatabase.release_date.desc()),
                'date_min': self.movies.order_by(MoviesDatabase.release_date)}

        self.movies = order_by[self.order]

    def filter_by(self):
        for selected_genre in self.genres:
            self.movies = self.movies.filter(MoviesDatabase.genre.contains(selected_genre))
        for selected_rating in self.rating:
            self.movies = self.movies.filter(MoviesDatabase.PG == selected_rating)
        print(self.rating)
        print('PG-13')

        #fix deleting items
        # for selected_critics in self.critics:
        #     self.movies = self.movies.filter(MoviesDatabase.certified.contains(selected_critics))

        # for selected_audience in self.audience:
        #     self.movies = self.movies.filter(MoviesDatabase.genre.contains(selected_genre))

        # self.movies = self.movies.filter_by(filters)
    def return_movies(self):
        self.search_by()
        self.order_by()
        self.filter_by()
        return self.movies[self.index:self.index + 5]
