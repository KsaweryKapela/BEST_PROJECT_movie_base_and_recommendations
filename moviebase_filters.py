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

        self.critics_dict = {
            'c-loved': MoviesDatabase.certified == 'certified-fresh',
            'c-liked': MoviesDatabase.certified == 'fresh',
            'c-hated': MoviesDatabase.certified == 'rotten',
            '': MoviesDatabase.title != 'Empty query'
        }

        self.audience_dict = {
            'a-liked': MoviesDatabase.user_score > 70,
            'a-hated': MoviesDatabase.user_score < 70,
            '': MoviesDatabase.title != 'Empty query'
        }

        self.search_dict = {'title': MoviesDatabase.title,
                            'collection': MoviesDatabase.collection,
                            'director': MoviesDatabase.director,
                            'cast': MoviesDatabase.cast,
                            'studio': MoviesDatabase.studio}

        self.order_dict = \
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

    # def find_key(self):
    #     try:
    #         searched_data = session['searched_data']
    #         session['searched_data'] = ''
    #         self.key = searched_data
    #     except KeyError:
    #         self.key = request.args.get('key')
    #     return self.key

    def search_by(self):

        self.movies = self.movies.filter(or_(
            self.search_dict[self.search].startswith(self.key),
            self.search_dict[self.search].contains(f' {self.key}')))

    def order_by(self):
        self.movies = self.order_dict[self.order]

    def filter_by(self):
        if self.rating == '':
            ratings = MoviesDatabase.PG != 'Non existing rating'
        else:
            ratings = MoviesDatabase.PG == self.rating

        self.movies = self.movies.filter(ratings, self.critics_dict.get(self.critics),
                                         self.audience_dict[self.audience])

        if self.genres != ['']:
            for chosen_genre in self.genres:
                self.movies = self.movies.filter(MoviesDatabase.genre.contains(chosen_genre))

    def return_movies(self):
        self.order_by()
        self.filter_by()
        self.search_by()

        return self.movies[self.index:self.index + 5]
