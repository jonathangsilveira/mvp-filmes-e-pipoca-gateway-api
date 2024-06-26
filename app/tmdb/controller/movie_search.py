from requests import get, Response
from typing import Optional

from app.tmdb.config import SERVER_URL
from app.tmdb.model.tmdb_search_result_model import TMDBMovieSearchResultsModel
from app.tmdb.controller.TMDBException import raise_for_tmdb_error

def search_movies(api_key: str, query: str, 
                  language: str, page: int = 1, 
                  year: Optional[int] = None) -> TMDBMovieSearchResultsModel:
    """
    Busca por filmes dado o termo e o ano.
    Retorna os resultados paginados.

    Parâmetros:
        api_key: Chave de acesso a API do TMDB.
        query: Termo usado na busca para encontrar filmes.
        language: Idioma de preferência para retorno dos dados.
        year: Ano de lançamento do filme.
        page: Página para exibir os resultados.
    """

    query_params = {
        'query': query, 
        'language': language, 
        'year': year, 'page': page, 
        'api_key': api_key
    }
    response: Response = get(
        url=f'{SERVER_URL}/search/movie', 
        params=query_params
    )
    raise_for_tmdb_error(response)
    body = response.json()
    return TMDBMovieSearchResultsModel(**body)
    