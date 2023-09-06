import sys
import dotenv
import os
dotenv.load_dotenv()
sys.path.append(os.getenv('MAINDIR'))
from main import MoviesDatabase, KeyWords, db
import pandas as pd
import numpy as np
from keybert import KeyBERT
from nltk.stem import WordNetLemmatizer
import nltk
import gensim.downloader


def get_namelist():
    baby_df = pd.read_csv('nlp_synopsis_exploration/babynames.csv')
    namelist = set(baby_df['Name'])
    return namelist

def remove_names(keyword_list, namelist):
    return [word for word in keyword_list if word.capitalize() not in namelist]

def lemmatize_keywords(keyword_list, lemmatizer):
    return [lemmatizer.lemmatize(word) for word in keyword_list]

def delete_unrecognized_keywords(keyword_list, word2vec):
    new_keyword_list = []
    for word in keyword_list:
        try:
           word2vec[word]
           new_keyword_list.append(word)
        except KeyError:
            pass
    return new_keyword_list

if __name__ == '__main__':
    
    title = [movie.title for movie in MoviesDatabase.query.all()]
    synopsis = [movie.description for movie in MoviesDatabase.query.all()]

    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(synopsis, keyphrase_ngram_range=(1, 1), top_n=10)

    keywords_words = []
    keywords_values = []

    for word_list in keywords:
        keywords_words.append([word[0] for word in word_list])
        keywords_values.append([word[1] for word in word_list])

    df = pd.DataFrame({'title': title, 'synopsis': synopsis, 'keywords': keywords_words, 'keyvalues': keywords_values})

    namelist = get_namelist()
    df['keywords'] = df['keywords'].apply(remove_names, args=(namelist,))

    lemmatizer = WordNetLemmatizer()

    df['keywords'] = df['keywords'].apply(lemmatize_keywords, args=(lemmatizer,))

    wv = gensim.downloader.load('glove-wiki-gigaword-300')
    df['keywords'] = df['keywords'].apply(delete_unrecognized_keywords, args=(wv,))

    separated_keywords = df.keywords.values

    all_keywords = set([word for sublist in separated_keywords for word in sublist])
    keywords_to_add = [KeyWords(word=word) for word in all_keywords]
    db.session.add_all(keywords_to_add)
    db.session.commit()

    # parent_words = []
    # child_words = []
    # connection_value = []

    # for word_1 in choosen_keywords:
    #     for word_2 in choosen_keywords:
    #         if word_1 == word_2:
    #             continue
    #         similarity = wv.similarity(word_1, word_2)
    #         if similarity > 0.5:
    #             parent_words.append(word_1)
    #             child_words.append(word_2)
    #             connection_value.append(similarity)