import requests
from main import MoviesDatabase, db, API_KEY

for movie in MoviesDatabase.query.filter_by(img_url='').all():
    repeat = True
    print(movie.id)
    char_to_replace = {'-': '',
                       '.': '',
                       ':': '',
                       '#': ''}
    final_movie = movie.title.translate(str.maketrans(char_to_replace)).lower()
    data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={final_movie}")
    if 'results' in data.json() and data.json()['results'] != []:
        for query in data.json()['results']:
            if 'release_date' in query and movie.release_date[-4:] == query['release_date'][0:4]:
                movie.img_url = f"https://image.tmdb.org/t/p/w500{query['poster_path']}"
                db.session.commit()
                repeat = False
                break

        if repeat:
            for query in data.json()['results']:
                if 'release_date' in query and query['release_date'] != '':
                    if int(movie.release_date[-4:]) + 1 >= int(query['release_date'][0:4]) >= int(movie.release_date[-4:]) - 1:
                        movie.img_url = f"https://image.tmdb.org/t/p/w500{query['poster_path']}"
                        db.session.commit()
                        repeat = False
                        break

        if repeat:
            movie.img_url = f"https://image.tmdb.org/t/p/w500{data.json()['results'][0]['poster_path']}"
            db.session.commit()
            repeat = False
        if movie.img_url == '':
            print(movie.title)

    else:
        print(movie.title + 'no results or empty results')
        