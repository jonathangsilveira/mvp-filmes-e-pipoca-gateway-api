from requests import put

from app.data.config import config

from app.schemas.schema_models import SuccessModel

def rate_movie(movie_id: int, rate_value: int) -> SuccessModel:
    """
    Define nota de avaliação para o filme.
    """
    request_body = {'rate_value': rate_value}
    response = put(
        url=f'{config.DATA_API_BASE_URL}/movie/rate/{movie_id}',
        json=request_body
    )
    response.raise_for_status()
    response_body = response.json()
    return SuccessModel(**response_body)