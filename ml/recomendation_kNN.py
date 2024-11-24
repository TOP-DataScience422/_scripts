from numpy import array
from pandas import (
    DataFrame,
    read_csv,
)
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

from pathlib import Path
from sys import path


movies_raw = read_csv(Path(path[0]) / 'movies.csv')
ratings_raw = read_csv(Path(path[0]) / 'ratings.csv')


ratings = ratings_raw.pivot(columns='user_id', index='movie_id', values='rating')

# movie_ratings_cnt = []
# for i in range(len(ratings.index)):
#     movie_ratings_cnt.append(ratings.iloc[i].count())
# movie_ratings_cnt = array(movie_ratings_cnt)

movie_ratings_cnt = ratings_raw.groupby('movie_id')['rating'].count()

# >>> sum(movie_ratings_cnt >= 10)
# 2269

# user_ratings_cnt = []
# for i in range(len(ratings.columns)):
#     user_ratings_cnt.append(ratings.iloc[:, i].count())
# user_ratings_cnt = array(user_ratings_cnt)

user_ratings_cnt = ratings_raw.groupby('user_id')['rating'].count()

# >>> sum(user_ratings_cnt >= 50)
# 385

movie_mask = movie_ratings_cnt[movie_ratings_cnt >= 10].index
user_mask = user_ratings_cnt[user_ratings_cnt >= 50].index

ratings = ratings.loc[movie_mask, :].loc[:, user_mask]
ratings.fillna(0, inplace=True)

# >>> ratings.shape
# (2269, 385)

ratings_csr = csr_matrix(ratings.values)


model = NearestNeighbors(
    n_neighbors=20,
    algorithm='brute',
    metric='cosine',
    n_jobs=-1
)
model.fit(ratings_csr)


word = 'Mask'

movies_contain_word = movies_raw['title'].str.contains(word)
movies_contain_word = movies_raw[movies_contain_word]

# >>> movies_contain_word
#       movie_id                                              title                                  genres
# 325        367                                   Mask, The (1994)             Action|Comedy|Crime|Fantasy
# 1331      1801                   Man in the Iron Mask, The (1998)                  Action|Adventure|Drama
# 1481      2006                          Mask of Zorro, The (1998)                   Action|Comedy|Romance
# 1965      2609              King of Masks, The (Bian Lian) (1996)                                   Drama
# 1978      2625                        Black Mask (Hak hap) (1996)  Action|Adventure|Crime|Sci-Fi|Thriller
# 2418      3213                Batman: Mask of the Phantasm (1993)                      Animation|Children
# 4444      6563                          Masked & Anonymous (2003)                            Comedy|Drama
# 5338      8880                                        Mask (1985)                                   Drama
# 5798     31698                             Son of the Mask (2005)       Adventure|Children|Comedy|Fantasy
# 6014     37857                                  MirrorMask (2005)        Adventure|Children|Drama|Fantasy
# 6553     54910  Behind the Mask: The Rise of Leslie Vernon (2006)                  Comedy|Horror|Thriller
# 9153    147657                             Masked Avengers (1981)

movie_index = movies_contain_word.iloc[0]['movie_id']

dist, idx = model.kneighbors(ratings_csr[movie_index], 5)

# >>> DataFrame([dist.flat, idx.flat])
#        0           1           2           3           4
# 0    0.0    0.393547    0.412042    0.438781    0.443503
# 1  367.0  402.000000  420.000000  449.000000  586.000000

mask = movies_raw.isin(idx.flat[1:])['movie_id']
print(movies_raw[mask])

#      movie_id                         title                        genres
# 364       420  Beverly Hills Cop III (1994)  Action|Comedy|Crime|Thriller
# 390       449    Fear of a Black Hat (1994)                        Comedy
# 504       586             Home Alone (1990)               Children|Comedy


