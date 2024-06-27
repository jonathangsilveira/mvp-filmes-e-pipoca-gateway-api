from .schemas.schema_models import MovieSearchSchemaModel
from .schemas.schema_models import MovieDetailsQuerySchema
from .schemas.schema_models import MovieDetailsPathSchema
from .schemas.schema_models import GetWatchlistQueryModel
from .schemas.schema_models import MovieSearchResultModel
from .schemas.schema_models import AddMovieToWatchlistPathModel
from .schemas.schema_models import RemoveMovieToWatchlistPathModel
from .tmdb.controller.movie_details import get_details
from .tmdb.controller.movie_search import search_movies
from .tmdb.controller.TMDBException import TMDBException
from .data.model import models
from .data.controller.watchlist import WatchlistController

TMDB_API_KEY = ''
