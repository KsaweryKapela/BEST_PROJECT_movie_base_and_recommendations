import json

from main import MoviesDatabase, Actors, db, Genres, Text, Directors, Writers
#
# # populating actors
# for movie in MoviesDatabase.query.all():
#     for cast_member in json.loads(movie.cast).items():
#         x = cast_member[1]
#         if x == 'Director' or x == 'Screenwriter' or x == 'Art Director' or x == 'Set Decoration' or x == 'Casting' or\
#                 x == 'Producer' or x == 'Executive Producer' or x == 'Original Music' or x == 'Film Editing'\
#                 or x == 'Writer'  or x == 'Cinematographer' or x == 'Production Design' or x == 'Costume Design'\
#                 or x == 'Film Editor' or x == 'Associate Producer' or x == 'Original Music and Songs' \
#                 or x == 'Co Editor' or x == 'Hair Stylist' or x == 'Makeup Artist' or x == 'Co Executive Producer'\
#                 or x == 'Co Producer':
#             pass
#         else:
#             if Actors.query.filter_by(name=cast_member[0]).first():
#                 print(Actors.query.filter_by(name=cast_member[0]).first().name)
#                 actor = Actors.query.filter_by(name=cast_member[0]).first()
#                 actor.plays_in.append(movie)
#
#
# # populating genres
# all_genres = []
# for gnr in MoviesDatabase.query.all():
#     for genre in gnr.genre.split(', '):
#         if genre in all_genres:
#             pass
#         else:
#             all_genres.append(genre)
#             new_genre = Genres(name=genre)
#             db.session.add(new_genre)
#
# for movie in MoviesDatabase.query.all():
#     for genre in movie.genre.split(', '):
#         movie_genre = Genres.query.filter_by(name=genre).first()
#         movie_genre.genre_of.append(movie)
#
#
# # populating PG_text
# all_PG_text = []
# for movie in MoviesDatabase.query.all():
#     correct_string = (movie.PG_text.replace('PG-13 ', '').replace('R ', '').replace('PG ', '').replace('(', '').
#                       replace(')', ''))
#     if 'TV' not in correct_string:
#         if len(correct_string) > 5:
#             for pg_text in correct_string.split('|'):
#                 if pg_text not in all_PG_text:
#                     all_PG_text.append(pg_text)
#                     new_text = Text(text=pg_text)
#                     db.session.add(new_text)
#
#
# for movie in MoviesDatabase.query.all():
#     text_list = []
#     for pg_text in movie.PG_text.replace('PG-13 ', '').replace('R ', '').replace('PG ', '')\
#             .replace('(', '').replace(')', '').split('|'):
#         if Text.query.filter_by(text=pg_text).first():
#             if pg_text in text_list:
#                 pass
#             else:
#                 text_list.append(pg_text)
#                 movie_text = Text.query.filter_by(text=pg_text).first()
#                 movie_text.text_of.append(movie)
#
#
# # populating directors
# all_directors = []
# for movie in MoviesDatabase.query.all():
#     for director in movie.director.split(', '):
#         if director in all_directors:
#             pass
#         else:
#             all_directors.append(director)
#             new_director = Directors(name=director)
#             db.session.add(new_director)
#
#
# for movie in MoviesDatabase.query.all():
#     for director in movie.director.split(', '):
#         movie_director = Directors.query.filter_by(name=director).first()
#         movie_director.directed.append(movie)
#
#
#
# # populating writers
# all_writers = []
# for movie in MoviesDatabase.query.all():
#     for writer in movie.writer.split(', '):
#         if writer in all_writers:
#             pass
#         else:
#             all_writers.append(writer)
#             new_writer = Writers(name=writer)
#             db.session.add(new_writer)
#
#
# for movie in MoviesDatabase.query.all():
#     for writer in movie.writer.split(', '):
#         movie_writer = Writers.query.filter_by(name=writer).first()
#         movie_writer.wrote.append(movie)