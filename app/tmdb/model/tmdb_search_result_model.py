from pydantic import BaseModel

from app.tmdb.model.tmdb_movie_search_model import TMDBMovieSearchResultModel

class TMDBMovieSearchResultsModel(BaseModel):
    """
    Modelo representando o resultado paginado da busca por filmes da API TMDB.
    """
    page: int
    total_pages: int
    total_results: int
    results: list[TMDBMovieSearchResultModel] = []