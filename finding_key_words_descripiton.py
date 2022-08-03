from rake_nltk import Rake

from main import MoviesDatabase

all_keywords = []
points = 0
for movie in MoviesDatabase.query.all():
    text = movie.description
    print(movie.title)
    r = Rake()
    r.extract_keywords_from_text(text)
    for keyword in r.get_ranked_phrases():
        if keyword in all_keywords:
            points += 1
            print(points)

        print(keyword)
        all_keywords.append(keyword)

print(points)
