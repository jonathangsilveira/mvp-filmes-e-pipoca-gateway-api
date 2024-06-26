from .schemas.schema_models import MovieSearchSchemaModel
from .schemas.schema_models import MovieDetailsQuerySchema
from .schemas.schema_models import MovieDetailsPathSchema
from .tmdb.model.tmdb_movie_details_model import TMDBMovieDetailsModel
from .tmdb.model.tmdb_genre_model import TMDBGenreModel
from .tmdb.model.tmdb_search_result_model import TMDBMovieSearchResultsModel
from .tmdb.model.tmdb_movie_search_model import TMDBMovieSearchResultModel
from .tmdb.controller.movie_details import get_details
from .tmdb.controller.movie_search import search_movies
from .tmdb.controller.TMDBException import TMDBException

TMDB_API_KEY = ''
