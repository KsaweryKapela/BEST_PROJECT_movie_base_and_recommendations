import time
from numerize import numerize
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import or_, cast, Integer, and_
from forms import *
from flask_login import UserMixin
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from functions import check_for_arrow

app = Flask(__name__)
API_KEY = "def26f3a5c5a48319f33d74bb1bd2009"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={"autoflush": False})
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    movies = db.relationship('UsersFilms', backref='users')


#many to many
class UsersFilms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies_database.id'), nullable=True)
    tag = db.Column(db.String(10), unique=False, nullable=True)

    def __repr__(self):
        return str(self.movie_id)


class MoviesDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_ids = db.relationship('UsersFilms', backref='movies_database')

    title = db.Column(db.String(300), unique=False, nullable=True)
    description = db.Column(db.String(5000), unique=False, nullable=True)
    genre = db.Column(db.String(3000), unique=False, nullable=True)
    director = db.Column(db.String(3000), unique=False, nullable=True)
    writer = db.Column(db.String(3000), unique=False, nullable=True)
    cast = db.Column(db.String(3000), unique=False, nullable=True)
    release_date = db.Column(db.String(500), unique=False, nullable=True)

    studio = db.Column(db.String(3000), unique=False, nullable=True)
    producer = db.Column(db.String(3000), unique=False, nullable=True)
    collection = db.Column(db.String(300), unique=False, nullable=True)

    tomatometer = db.Column(db.Integer, unique=False, nullable=True)
    critic_reviews_no = db.Column(db.Integer, unique=False, nullable=True)
    user_score = db.Column(db.Integer, unique=False, nullable=True)
    user_reviews_no = db.Column(db.Integer, unique=False, nullable=True)
    certified = db.Column(db.String(100), unique=False, nullable=True)

    boxoffice = db.Column(db.Integer, unique=False, nullable=True)
    runtine = db.Column(db.String(100), unique=False, nullable=True)

    PG = db.Column(db.String(100), unique=False, nullable=True)
    PG_text = db.Column(db.String(1000), unique=False, nullable=True)
    img_url = db.Column(db.String(500), unique=False, nullable=True)
    rotten_url = db.Column(db.String(500), unique=False, nullable=True)

    computed_audience_score = db.Column(db.Integer, unique=False, nullable=True)
    computed_critic_score = db.Column(db.Integer, unique=False, nullable=True)


class UserSuggestion(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=False, nullable=True)
    computed_audience_score = db.Column(db.Integer, unique=False, nullable=True)
    computed_critic_score = db.Column(db.Integer, unique=False, nullable=True)
    points = db.Column(db.Integer, unique=False, nullable=True)
    img_url = db.Column(db.String(500), unique=False, nullable=True)


movie_actors = db.Table('movie_actors',
                        db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
                        db.Column('movie_id', db.Integer, db.ForeignKey('movies_database.id')))


user_movie_actors = db.Table('user_movie_actors',
                        db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
                        db.Column('user_movie_id', db.Integer, db.ForeignKey('users_films.id')))


class Actors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    plays_in = db.relationship('MoviesDatabase', secondary=movie_actors, backref='actors')
    users_movie_plays = db.relationship('UsersFilms', secondary=user_movie_actors, backref='users_actors')

    def __repr__(self):
        return str(self.id)


movie_genres = db.Table('movie_genres',
                        db.Column('genre_id', db.Integer, db.ForeignKey('genres.id')),
                        db.Column('movie_id', db.Integer, db.ForeignKey('movies_database.id')))


class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    genre_of = db.relationship('MoviesDatabase', secondary=movie_genres, backref='genres')


movie_text = db.Table('movie_text',
                        db.Column('text_id', db.Integer, db.ForeignKey('text.id')),
                        db.Column('movie_id', db.Integer, db.ForeignKey('movies_database.id')))


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=False, nullable=True)
    text_of = db.relationship('MoviesDatabase', secondary=movie_text, backref='text')


movie_directors = db.Table('movie_directors',
                        db.Column('director_id', db.Integer, db.ForeignKey('directors.id')),
                        db.Column('movie_id', db.Integer, db.ForeignKey('movies_database.id')))


class Directors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    directed = db.relationship('MoviesDatabase', secondary=movie_directors, backref='director_of')


movie_writers = db.Table('movie_writers',
                        db.Column('writer_id', db.Integer, db.ForeignKey('writers.id')),
                        db.Column('movie_id', db.Integer, db.ForeignKey('movies_database.id')))


class Writers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    wrote = db.relationship('MoviesDatabase', secondary=movie_writers, backref='writer_of')


db.create_all()


@app.context_processor
def header():
    form = SearchForm()
    return dict(search_form=form)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route("/", methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return redirect('favorites/1')

    return render_template("index.html")


@app.route('/favorites/<int:index>', methods=['GET', 'POST'])
def favorites(index):
    movies = UsersFilms.query.filter_by(user_id=current_user.id).filter_by(tag='heart')[index * 7 - 7:index * 7 + 1]
    if index != 1 and movies == []:
        return redirect(f'/favorites/{index - 1}')

    for movie in movies:
        session[f'movie{movies.index(movie)}'] = movie.movie_id

    return render_template("index.html", movies=movies, right_arrow=check_for_arrow(movies))


@app.route('/watch-list/<int:index>', methods=['GET', 'POST'])
def watch_list(index):
    movies = UsersFilms.query.filter_by(user_id=current_user.id).filter_by(tag='bookmark')[index * 7 - 7:index * 7 + 1]

    if index != 1 and movies == []:
        return redirect(f'/favorites/{index - 1}')

    for movie in movies:
        session[f'movie{movies.index(movie)}'] = movie.movie_id

    return render_template("index.html", movies=movies, right_arrow=check_for_arrow(movies))


@app.route('/disliked/<int:index>', methods=['GET', 'POST'])
def disliked(index):
    movies = UsersFilms.query.filter_by(user_id=current_user.id).filter_by(tag='dislike')[index * 7 - 7:index * 7 + 1]

    if index != 1 and movies == []:
        return redirect(f'/favorites/{index - 1}')

    for movie in movies:
        session[f'movie{movies.index(movie)}'] = movie.movie_id

    return render_template("index.html", movies=movies, right_arrow=check_for_arrow(movies))


@app.route('/ignored/<int:index>', methods=['GET', 'POST'])
def ignored(index):
    movies = UsersFilms.query.filter_by(user_id=current_user.id).filter_by(tag='ignore')[index * 7 - 7:index * 7 + 1]
    if index != 1 and movies == []:
        return redirect(f'/favorites/{index - 1}')
    for movie in movies:
        session[f'movie{movies.index(movie)}'] = movie.movie_id

    return render_template("index.html", movies=movies, right_arrow=check_for_arrow(movies))


@app.route('/waypoint')
def way_point():
    correct_url = session['redirect_link']
    session['redirect_link'] = None
    return redirect(correct_url)


@app.route('/wall/<username>', methods=['GET', 'POST'])
def wall(username):
    if current_user.is_authenticated and username == current_user.username:
        return redirect('/')

    user = Users.query.filter_by(username=username).first()
    movies = UsersFilms.query.filter_by(user_id=user.id).all()

    return render_template("wall.html", movies=movies, username=username)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(email=form.email.data,
                         username=form.username.data,
                         password=form.password.data
                         )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if Users.query.filter_by(email=form.email.data).first():
            if Users.query.filter_by(password=form.password.data).first():
                login_user(Users.query.filter_by(email=form.email.data).first())
                return redirect('/')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/edit_user_lists', methods=['GET'])
def edit_user_lists():
    index = int(request.args.get('value'))
    list_type = request.args.get('command2')
    command = request.args.get('command')
    list_types = ['heart', 'bookmark', 'dislike', 'ignore']

    for icon_type in list_types:
        if icon_type == list_type:

            if command == 'add':
                if UsersFilms.query.filter(and_(UsersFilms.user_id == current_user.id),
                                           (UsersFilms.movie_id == session[f'movie{index}'])).first():
                    UsersFilms.query.filter(and_(UsersFilms.user_id == current_user.id),
                                            (UsersFilms.movie_id == session[f'movie{index}'])).first().tag = list_type


                else:
                    movie = UsersFilms(user_id=current_user.id, movie_id=session[f'movie{index}'], tag=list_type)
                    db.session.add(movie)
                    for actor in MoviesDatabase.query.filter_by(id=session[f'movie{index}']).first().actors:
                        actor = Actors.query.filter_by(id=actor.id).first()
                        actor.users_movie_plays.append(movie)


            elif command == 'del':
                movies = UsersFilms.query.filter(and_(UsersFilms.user_id == current_user.id),
                                                 (UsersFilms.movie_id == session[f'movie{index}']),
                                                 (UsersFilms.tag == list_type)).all()

                for movie in movies:
                    db.session.delete(movie)

    if command == "rDel":
        movies = UsersFilms.query.filter(and_(UsersFilms.user_id == current_user.id),
                                         (UsersFilms.movie_id == session[f'movie{index}'])).all()
        for movie in movies:
            db.session.delete(movie)

        session['redirect_link'] = list_type

    elif command == 'recAdd':

        movie = UsersFilms(user_id=current_user.id, movie_id=session['recommendations_movie_id'], tag=list_type)

        for actor in MoviesDatabase.query.get(session['recommendations_movie_id']).actors:
            actor = Actors.query.filter_by(id=actor.id).first()
            actor.users_movie_plays.append(movie)

        db.session.add(movie)

    db.session.commit()
    return {'success': 'yay'}


@app.route('/searchUsers', methods=['POST', 'GET'])
def search_users():
    form = SearchForm()
    if form.validate_on_submit:
        if Users.query.filter_by(username=form.searched.data).first():
            return redirect(f'/wall/{form.searched.data}')
        else:
            users_list = [user.username for user in Users.query.all()
                          if user.username.lower().startswith(form.searched.data.lower())]
            return render_template('select_user.html', data=users_list)


@app.route('/searchFilms', methods=['POST', 'GET'])
def search_films():
    form = SearchForm()
    if form.validate_on_submit:
        if MoviesDatabase.query.filter_by(title=form.searched.data).first():
            movie = MoviesDatabase.query.filter_by(title=form.searched.data).first()
            new_movie = UsersFilms(user_id=current_user.id, movie_id=movie.id, tag='heart')
            db.session.add(new_movie)

            for actor in MoviesDatabase.query.filter_by(id=movie.id).first().actors:
                actor = Actors.query.filter_by(id=actor.id).first()
                print(actor)
                actor.users_movie_plays.append(new_movie)

            db.session.commit()
        else:
            session['searched_data'] = form.searched.data
            return redirect(url_for('movie_base'))
    return redirect('/')


@app.route('/moviebase', methods=['GET', 'POST'])
def movie_base():
    return render_template('movie_base.html', hide="True")


@app.route('/fetch_movies', methods=['GET'])
def fetch_movies():
    value = request.args.get('value')
    movie_list = MoviesDatabase.query.filter(or_(
        MoviesDatabase.title.startswith(value),
        MoviesDatabase.title.contains(f' {value}') if len(value) > 1 else None)) \
                     .order_by(cast(MoviesDatabase.computed_critic_score, Integer).desc())[:7]

    titles_list = [movie.title for movie in movie_list]
    return {'movie_list': titles_list}


@app.route('/fetch_users', methods=['GET', 'POST'])
def fetch_users():
    usernames_list = [user.username for user in Users.query.all()]
    return {'list': usernames_list[0:7]}


@app.route('/fetch_moviebase', methods=['GET'])
def fetch_database():
    try:
        searched_data = session['searched_data']

    except KeyError:
        session['searched_data'] = ''
        searched_data = session['searched_data']

    if searched_data == '':
        key = request.args.get('key')
    else:
        key = searched_data

    search = request.args.get('search')
    hits = request.args.get('hits')
    value = int(request.args.get('index'))
    rotten = request.args.get('rotten')
    liked = request.args.get('liked')
    new = request.args.get('new')
    certified = request.args.get('certified')

    if search == 'title':
        movies = MoviesDatabase.query.filter(or_(
            MoviesDatabase.title.startswith(key),
            MoviesDatabase.title.contains(f' {key}')))

    elif search == 'collection':
        movies = MoviesDatabase.query.filter(or_(
            MoviesDatabase.collection.startswith(key),
            MoviesDatabase.collection.contains(f' {key}')))

    elif search == 'director':
        movies = MoviesDatabase.query.filter(or_(
            MoviesDatabase.director.startswith(key),
            MoviesDatabase.director.contains(f' {key}')))

    elif search == 'cast':
        movies = MoviesDatabase.query.filter(or_(
            MoviesDatabase.cast.startswith(key),
            MoviesDatabase.cast.contains(key)))

    elif search == 'studio':
        movies = MoviesDatabase.query.filter(or_(
            MoviesDatabase.studio.startswith(key),
            MoviesDatabase.studio.contains(f' {key}')))

    if certified == 'True':
        movies = movies.filter(MoviesDatabase.certified == 'certified-fresh')

    if rotten == 'False':
        movies = movies.filter(MoviesDatabase.tomatometer != '').order_by(
            cast(MoviesDatabase.computed_critic_score, Integer))

    elif hits == 'True':
        movies = movies.filter(MoviesDatabase.boxoffice != '0').order_by(cast(MoviesDatabase.boxoffice, Integer).
                                                                         desc())
    elif hits == 'False':
        movies = movies.filter(MoviesDatabase.boxoffice != '0').order_by(cast(MoviesDatabase.boxoffice, Integer))

    elif liked == 'True':
        movies = movies.order_by(cast(MoviesDatabase.computed_audience_score, Integer).
                                 desc())
    elif liked == 'False':
        movies = movies.filter(MoviesDatabase.user_score != '').order_by(
            cast(MoviesDatabase.computed_audience_score, Integer))

    elif new == 'True':
        movies = movies.order_by(MoviesDatabase.release_date.desc())

    elif new == 'False':
        movies = movies.order_by(MoviesDatabase.release_date)

    else:
        movies = movies.filter(MoviesDatabase.tomatometer != '').order_by(
            cast(MoviesDatabase.computed_critic_score, Integer).
                desc())

    movies = movies[value:value + 5]

    index_of_favorite = []
    index_of_bookmarks = []
    index_of_dislikes = []
    index_of_ignores = []

    if current_user.is_authenticated:

        for movie in movies[:4]:
            session[f'movie{movies.index(movie)}'] = movie.id

            if UsersFilms.query.filter_by(user_id=current_user.id).filter_by(movie_id=movie.id).filter_by(
                    tag='heart').first():
                index_of_favorite.append(movies.index(movie))

            if UsersFilms.query.filter_by(user_id=current_user.id).filter_by(movie_id=movie.id).filter_by(
                    tag='bookmark').first():
                index_of_bookmarks.append(movies.index(movie))

            if UsersFilms.query.filter_by(user_id=current_user.id).filter_by(movie_id=movie.id).filter_by(
                    tag='dislike').first():
                index_of_dislikes.append(movies.index(movie))

            if UsersFilms.query.filter_by(user_id=current_user.id).filter_by(movie_id=movie.id).filter_by(
                    tag='ignore').first():
                index_of_ignores.append(movies.index(movie))

    movie_url = [movie.img_url for movie in movies]
    movie_title = [movie.title.replace('--', '-') for movie in movies]
    movie_date = [movie.release_date[:4] for movie in movies]
    movie_genre = [movie.genre for movie in movies]
    movie_description = [movie.description if len(movie.description) < 250 else movie.description[:250] + '...' for
                         movie in movies]
    movie_director = ['Directed by ' + movie.director for movie in movies]
    movie_cast = [movie.cast for movie in movies]
    movie_studio = ['Produced by ' + movie.studio.split(', ')[0] if movie.studio != '' else '' for movie in movies]
    movie_boxoffice = [
        "Grossed " + numerize.numerize(int(movie.boxoffice)) + " in USA" if movie.boxoffice != '0' else '' for movie in
        movies]
    movie_runtime = [movie.runtine for movie in movies]
    movie_tomatometer = [movie.tomatometer + '%' if movie.tomatometer != '' else '-' for movie in movies]
    movie_audience = [movie.user_score + '%' if movie.user_score != '' else '-' for movie in movies]

    return {'movie_url': movie_url,
            'movie_title': movie_title,
            'movie_date': movie_date,
            'movie_genre': movie_genre,
            'movie_description': movie_description,
            'movie_director': movie_director,
            'movie_cast': movie_cast,
            'movie_studio': movie_studio,
            'movie_boxoffice': movie_boxoffice,
            'movie_runtime': movie_runtime,
            'movie_tomatometer': movie_tomatometer,
            'movie_audience': movie_audience,
            'key': key,
            'add-movie': index_of_favorite,
            'watch-list': index_of_bookmarks,
            'dislike': index_of_dislikes,
            'ignore': index_of_ignores,
            }


@app.route('/recommend', methods=['GET', 'POST'])
def recommendation_page():
    return render_template('recommend.html')


@app.route('/fetch_recommend', methods=['GET', 'POST'])
def fetch_recommend():
    from recomendations import MovieRecommendations

    recommend = MovieRecommendations()
    movie_id = recommend.update_recommendations(current_user.id)
    print(movie_id)
    session['recommendations_movie_id'] = movie_id
    movie = MoviesDatabase.query.get(movie_id)

    return {'movie_url': movie.img_url}


if __name__ == "__main__":
    app.run(port=1000, debug=True)
