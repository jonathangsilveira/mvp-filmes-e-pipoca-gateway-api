from requests import get, Response, HTTPError
from typing import Optional

from app.tmdb.config import SERVER_URL
from app.tmdb.model.paged_search_result_model import PagedSearchResultModel
from app.tmdb.controller.TMDBException import raise_for_tmdb_error

def search_movies(api_key: str, query: str, 
                  language: str, page: int = 1, 
                  year: Optional[int] = None) -> PagedSearchResultModel:
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
    response: Response = get(
        url=f'{SERVER_URL}/search/movie', 
        params={'query': query, 'language': language, 
                'year': year, 'page': page, 
                'api_key': api_key}
    )
    raise_for_tmdb_error(response)
    data = response.json()
    return PagedSearchResultModel(**data)
    