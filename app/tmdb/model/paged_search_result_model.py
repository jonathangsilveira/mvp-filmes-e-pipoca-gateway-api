from pydantic import BaseModel

from app.tmdb.model.movie_search_model import MovieSearchModel

class PagedSearchResultModel(BaseModel):
    """
    Modelo representando o resultado paginado da busca por filmes da API TMDB.
    """
    page: int
    total_pages: int
    total_results: int
    results: list[MovieSearchModel] = []