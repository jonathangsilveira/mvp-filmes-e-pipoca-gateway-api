from requests import get, Response

from app.tmdb.config import SERVER_URL
from app.tmdb.model.tmdb_movie_details_model import TMDBMovieDetailsModel
from app.tmdb.controller.TMDBException import raise_for_tmdb_error

def get_details(api_key: str, movie_id: int, language: str) -> TMDBMovieDetailsModel: 
    """
    Retorna detalhes do filme em TMDB API.
    """
    query_params = {'api_key': api_key, 'language': language}
    response: Response = get(
        url=f'{SERVER_URL}/movie/{movie_id}', 
        params=query_params
    )
    raise_for_tmdb_error(response)
    body = response.json()
    return TMDBMovieDetailsModel(**body)