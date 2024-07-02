from .schemas.schema_models import *
from .tmdb.controller.movie_details import get_details
from .tmdb.controller.movie_search import search_movies
from .tmdb.controller.trending_movies import get_trending_movies
from .tmdb.controller.TMDBException import TMDBException
from .data.model import models
from .data.controller.watchlist import WatchlistController
from .data.controller.rate_movie import rate_movie

TMDB_API_KEY = ''
