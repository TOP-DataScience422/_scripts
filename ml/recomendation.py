from pandas import read_csv

from pathlib import Path
from sys import path


movies = read_csv(Path(path[0]) / 'movies.csv')
ratings = read_csv(Path(path[0]) / 'ratings.csv')


mean_rating_by_movie = ratings.groupby('movie_id')['rating'].mean()
top_10 = mean_rating_by_movie.sort_values(ascending=False).iloc[:10]

mask = movies.isin(top_10.index)['movie_id']
print(movies[mask])

#       movie_id                                      title                    genres
# 4246      6192  Open Hearts (Elsker dig for evigt) (2002)                   Romance
# 4251      6201                           Lady Jane (1986)             Drama|Romance
# 7656     88448      Paper Birds (Pájaros de papel) (2010)              Comedy|Drama
# 8107    100556                 Act of Killing, The (2012)               Documentary
# 8148    102084               Justice League: Doom (2012)   Action|Animation|Fantasy
# 8154    102217             Bill Hicks: Revelations (1993)                    Comedy
# 9083    143031                            Jump In! (2007)      Comedy|Drama|Romance
# 9094    143511                               Human (2015)               Documentary
# 9096    143559                        L.A. Slasher (2015)      Comedy|Crime|Fantasy
# 9122    145994                     Formula of Love (1984)                    Comedy



