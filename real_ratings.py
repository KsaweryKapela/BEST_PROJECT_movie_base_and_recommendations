from main import MoviesDatabase, db

# Calculating scores with number of votes included, using a method inspired by Bayesian probability.

R = 60
W = 1000

for movie in MoviesDatabase.query.all():
    if movie.user_score != '' and movie.user_reviews_no != '' and movie.user_reviews_no != '0':
        try:
            real_score = (R * W + int(movie.user_score) * int(movie.user_reviews_no)) / (W + int(movie.user_reviews_no))
            movie.computed_audience_score = round(real_score)
        except ValueError:
            print(movie.title)

R = 60
W = 50

for movie in MoviesDatabase.query.all():
    try:
        if movie.tomatometer != '' and movie.critic_reviews_no != '':
            real_score = (R * W + int(movie.tomatometer) * int(movie.critic_reviews_no)) / (
                        W + int(movie.critic_reviews_no))
            movie.computed_critic_score = round(real_score)
    except ValueError:
        print(movie.title)

db.session.commit()
