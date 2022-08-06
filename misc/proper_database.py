class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    movies = db.relationship('UserMovie', backref='user')


class UserMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=True)
    tag = db.Column(db.String(10), unique=False, nullable=True)

    def __repr__(self):
        return str(self.movie_id)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_ids = db.relationship('UserMovie', backref='movie')

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


movie_actor = db.Table('movie_actor',
                       db.Column('actor_id', db.Integer, db.ForeignKey('actor.id')),
                       db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))

user_movie_actor = db.Table('user_movie_actor',
                            db.Column('actor_id', db.Integer, db.ForeignKey('actor.id')),
                            db.Column('user_movie_id', db.Integer, db.ForeignKey('user_movie.id')))


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    plays_in = db.relationship('Movie', secondary=movie_actor, backref='actor')
    user_movie_plays = db.relationship('UserMovie', secondary=user_movie_actor, backref='user_actor')

    def __repr__(self):
        return str(self.id)


movie_genre = db.Table('movie_genre',
                       db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
                       db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    genre_of = db.relationship('Movie', secondary=movie_genre, backref='movie_genre')


movie_text = db.Table('movie_text',
                      db.Column('text_id', db.Integer, db.ForeignKey('text.id')),
                      db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=False, nullable=True)
    text_of = db.relationship('Movie', secondary=movie_text, backref='text')


movie_director = db.Table('movie_director',
                          db.Column('director_id', db.Integer, db.ForeignKey('director.id')),
                          db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    directed = db.relationship('Movie', secondary=movie_director, backref='director_of')


movie_writer = db.Table('movie_writer',
                        db.Column('writer_id', db.Integer, db.ForeignKey('writer.id')),
                        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))


class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=False, nullable=True)
    wrote = db.relationship('Movie', secondary=movie_writer, backref='writer_of')
