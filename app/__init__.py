from .schemas.schema_models import BuscaPorTermoSchemaModel
from .schemas.schema_models import MovieDetailsSchemaModel
from .tmdb.model.movie_details_model import MovieDetailsModel
from .tmdb.model.genre_model import GenreModel
from .tmdb.controller.movie_details import get_details

TMDB_API_KEY = ''
TMDB_IMAGE_URL = 'https://image.tmdb.org/t/p/original'