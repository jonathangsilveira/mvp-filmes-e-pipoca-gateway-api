from requests import get, Response

from app.tmdb.config import SERVER_URL
from app.tmdb.model.movie_details_model import MovieDetailsModel

def get_details(api_key: str, movie_id: int, language: str) -> MovieDetailsModel: 
    """
    Retorna detalhes do filme em TMDB API.
    """
    response: Response = get(
        url=f'{SERVER_URL}/movie/{movie_id}', 
        params={'api_key': api_key, 'language': language}
    )
    response.raise_for_status()
    data = response.json()
    return MovieDetailsModel(**data)