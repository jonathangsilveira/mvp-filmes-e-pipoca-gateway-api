from requests import get, Response
from typing import Optional

from app.tmdb.config import SERVER_URL
from app.tmdb.model.tmdb_trending_movies import TMDBTrendingMoviesModel, TMDBTrendingMoviesResultModel
from app.tmdb.controller.TMDBException import raise_for_tmdb_error

def get_trending_movies(api_key: str, language: str, 
                        time_window: Optional[str] = None) -> TMDBTrendingMoviesResultModel:
    """
    Consulta os filmes que estão em alta dado um período de tempo.

    Parâmetros:
        api_key: Chave de acesso a API do TMDB.
        language: Idioma de preferência para retorno dos dados.
        time_window: Janela de tempo. Ex.: 'day' ou 'week'.
    """
    query_params = {
        'language': language, 
        'api_key': api_key
    }
    response: Response = get(
        url=f'{SERVER_URL}/trending/movie/{time_window}', 
        params=query_params
    )
    raise_for_tmdb_error(response)
    body = response.json()
    return TMDBTrendingMoviesResultModel(**body)