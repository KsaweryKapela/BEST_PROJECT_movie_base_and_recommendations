import itertools
import json
import math
import re
from collections import Counter
import sqlalchemy
from sqlalchemy import and_
from main import MoviesDatabase, UsersFilms, db, UserSuggestion, Actors



def give_points(list_name, points, movie_type):
    result = 0
    for item in list_name:
        if str(item) in movie_type:
            result += points
    return result


def update_recommendations(user_id):

    UserSuggestion.query.delete()
    db.session.commit()

    list_to_avoid = ['Seq.', 'of', 'and', 'Behavior', 'Some', 'Use', '', 'Strong', 'Images',
                     'References', 'Material', 'Graphic', 'Brief', 'Thematic']

    all_audience, all_critic = 0, 0

    all_pg, all_directors, all_writers, main_cast, supporting_cast, \
        all_critic_no, all_genres, all_dates = ([] for item in range(8))

    # to fix
    movie_list = [MoviesDatabase.query.get(movie.movie_id) for movie in
                  UsersFilms.query.filter_by(user_id=user_id).filter_by(tag='heart').all()]

    for movie in movie_list:
        x = 0
        for actor in MovieCast.query.filter_by(movie_id=movie.id).all():
            if x < 2:
                main_cast.append(actor.actor)

            elif x < 5:
                supporting_cast.append(actor.actor)
            x += 1

        all_writers += movie.writer.split(',')
        all_critic_no += list(
            range(math.ceil(int(movie.critic_reviews_no) - 25), math.floor(int(movie.critic_reviews_no) + 25) + 1))
        all_directors += movie.director.split(',')
        refined_PG = movie.PG_text.replace('(', '').replace(')', '').replace('|', ' ')

        for pg in refined_PG.split(" "):
            if pg in list_to_avoid:
                pass
            else:
                all_pg.append(pg)

        for genre in movie.genre.split(" "):
            all_genres.append(genre)

        all_dates += list(
            range(math.ceil(int(movie.release_date[:4]) - 1), math.floor(int(movie.release_date[:4]) + 1) + 1))

        all_audience += int(movie.computed_audience_score)
        all_critic += int(movie.computed_critic_score)

    if all_audience > all_critic:
        print('audience')
    else:
        print('critics')

    for movie in MoviesDatabase.query.filter(MoviesDatabase.computed_critic_score > 70).all()[:100]:
        #klasa recommendations
        movie_points = 0

        if UsersFilms.query.filter_by(user_id=user_id).filter_by(movie_id=movie.id).all():
            continue

        if movie.computed_critic_score:
            movie_points += movie.computed_critic_score * 2

        if movie.computed_audience_score:
            movie_points += movie.computed_audience_score * 2

        movie_points += give_points(all_genres, 50, movie.genre)
        movie_points += give_points(all_directors, 100, movie.director)
        movie_points += give_points(all_writers, 50, movie.writer)
        movie_points += give_points(main_cast, 100, movie.cast)
        movie_points += give_points(supporting_cast, 50, movie.cast)
        movie_points += give_points(all_pg, 5, movie.PG_text)
        movie_points += give_points(all_critic_no, 20, movie.critic_reviews_no)

        for year in all_dates:
            if year == int(movie.release_date[:4]):
                movie_points += 15

        new_movie = UserSuggestion(points=movie_points, title=movie.title, computed_critic_score=movie.
                                   computed_critic_score, computed_audience_score=movie.computed_audience_score)
        db.session.add(new_movie)

    db.session.commit()
