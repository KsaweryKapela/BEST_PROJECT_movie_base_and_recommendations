import itertools
import json
import requests
from bs4 import BeautifulSoup
from sqlalchemy import cast, Integer
from main import MoviesDatabase, db, MovieCast
import re


def cast_member(index):
    return re.sub('[^a-zA-Z]+', ' ', movie.cast.split(',')[index]).replace(' ', '', 1)[:-1]

movie_urls = []
#DEADLY HALLOWS p2, shrek forever, call me by your name, FULL METAL JACKET, Uncut Gems, Obscure object of desire

for movie_url in movie_urls:
    movie_url = movie_url

    try:
        page = requests.get(movie_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find("h1", class_="scoreboard__title").text
        genre = soup.find('div', class_='genre').text

    except:
        continue

    description = soup.find('div', id='movieSynopsis').text

    director = ""
    producer = ""
    runtime = ""
    collection = ""
    studio = ""
    writer = ""
    boxoffice = ""
    PG_text = ""

    user_reviews_no = soup.find('a', {'slot': 'audience-count'}).text
    certified = soup.find('score-board')['tomatometerstate']
    tomatometer = soup.find('score-board')['tomatometerscore']
    audience_score = soup.find('score-board')['audiencescore']
    critic_reviews_no = soup.find('a', class_='scoreboard__link--tomatometer').text
    PG = soup.find('score-board')['rating']
    time_ = soup.find_all('time')
    release_date = time_[0].text
    rotten_link = movie_url

    meta_rows = soup.find_all('li', class_="meta-row")
    for row in meta_rows:
        if row.find('div', class_="meta-label").text == 'Producer:':
            producer = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'Writer:':
            writer = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'Distributor:':
            studio = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'View the collection:':
            collection = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'Runtime:':
            runtime = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'Box Office (Gross USA):':
            boxoffice = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'Rating:':
            PG_text = row.find('div', class_="meta-value").text

        if row.find('div', class_="meta-label").text == 'Director:':
            director = row.find('div', class_="meta-value").text

    cast = soup.find_all('div', class_="media-body")
    final_cast = []
    for member in cast:
        cast_member = member.find_all('span')
        for span in cast_member:
            final_cast.append(span.text.replace('  ', '').replace('\n', ''))

    new_movie = MoviesDatabase(
        title=title,
        description=description.replace('  ', '').replace('\n', ''),
        genre=genre.replace('  ', '').replace('\n', ''),
        director=director.replace('  ', '').replace('\n', ''),
        writer=writer.replace('  ', '').replace('\n', ''),
        cast=str(final_cast),
        release_date=release_date.replace('  ', '').replace('\n', ''),

        studio=studio.replace('  ', '').replace('\n', ''),
        producer=producer.replace('  ', '').replace('\n', ''),
        collection=collection.replace('  ', '').replace('\n', ''),

        tomatometer=tomatometer,
        critic_reviews_no=critic_reviews_no,
        user_score=audience_score,
        user_reviews_no=user_reviews_no,
        certified=certified,

        boxoffice=boxoffice,
        runtine=runtime.replace('  ', '').replace('\n', ''),

        PG=PG,
        PG_text=PG_text.replace('  ', '').replace('\n', ''),
        img_url='',
        rotten_url=rotten_link)

    db.session.add(new_movie)
    db.session.commit()

# cleaning up database

for movie in MoviesDatabase.query.all():
    movie_description = MoviesDatabase.query.filter_by(description=movie.description).all()
    try:
        movie_description[1].description
        db.session.delete(MoviesDatabase.query.filter_by(description=movie.description).first())
        print(movie.title + ' CLONE')
    except:
        pass
    cast_list = movie.cast.split(', ')
    if 'xa0' in cast_list[0]:
        del cast_list[0]
        cast_string = ' '.join(cast_list)
        cast_string = '[' + cast_string.replace("' '", "', '")
        movie.cast = cast_string
    movie.user_reviews_no = re.sub("[^0-9]", "", movie.user_reviews_no)
    movie.boxoffice = movie.boxoffice.replace('M', '00000').replace('K', '00').replace('.', '').replace('$', '')
    raw_date = movie.release_date[-4:] + '-' + movie.release_date[:-6].replace(' ', '-')
    if len(raw_date) == 10:
        raw_date = raw_date.split('-')
        raw_date[-1] = '0' + raw_date[-1]
        raw_date = '-'.join(raw_date)
    chunks_to_replace = {'Jan': '01',
                         'Feb': '02',
                         'Mar': '03',
                         'Apr': '04',
                         'May': '05',
                         'Jun': '06',
                         'Jul': '07',
                         'Aug': '08',
                         'Sep': '09',
                         'Oct': '10',
                         'Nov': '11',
                         'Dec': '12'}
    for month, number in chunks_to_replace.items():
        if month in raw_date:
            raw_date = raw_date.replace(month, number)
            movie.release_date = raw_date


    cast_dict = {}
    for index in range(0, len(movie.cast), 2):
        try:
            print(cast_member(index))
            cast_dict[cast_member(index)] = cast_member(index + 1)
        except IndexError:
            continue
    print(cast_dict)
    cast_string = json.dumps(cast_dict)
    movie.cast = cast_string
db.session.commit()


for movie in MoviesDatabase.query.all():

    json_cast = json.loads(movie.cast)

    final_list = []

    for x, y in json_cast.items():
        if "Director" in (y, x) or "Screenwriter" in (y, x) or "Producer" in (y, x) or "Film Editor" in (y, x) or "Executive Producer" in (y, x):
            break
        else:
            final_list.append(x)

    for actor in final_list:

        new_cast = MovieCast(movie_id=movie.id, actor=actor)
        db.session.add(new_cast)

db.session.commit()


# Dinner in America, ['self',], fix cast [, Your Name, Cuties, Spiderman, The exortist box office, super img_url,
# piranha 2 release date, junun PTA Intouchables, Perfect Strangers, Moon miniaturka, paddington img_url,
# snowpiercer img_url

