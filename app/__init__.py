from .schemas.schema_models import MovieSearchSchemaModel
from .schemas.schema_models import MovieDetailsSchemaModel
from .tmdb.model.movie_details_model import MovieDetailsModel
from .tmdb.model.genre_model import GenreModel
from .tmdb.model.paged_search_result_model import PagedSearchResultModel
from .tmdb.model.movie_search_model import MovieSearchModel
from .tmdb.controller.movie_details import get_details
from .tmdb.controller.movie_search import search_movies
from .tmdb.controller.TMDBException import TMDBException

TMDB_API_KEY = ''
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/original'