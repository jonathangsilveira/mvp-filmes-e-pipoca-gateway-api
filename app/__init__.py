from .schemas.schema_models import MovieSearchSchemaModel
from .schemas.schema_models import MovieDetailsQuerySchema
from .schemas.schema_models import MovieDetailsPathSchema
from .tmdb.controller.movie_details import get_details
from .tmdb.controller.movie_search import search_movies
from .tmdb.controller.TMDBException import TMDBException

TMDB_API_KEY = ''
