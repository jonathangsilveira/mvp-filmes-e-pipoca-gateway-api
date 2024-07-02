from pydantic import BaseModel
from typing import Optional

class TMDBTrendingMoviesModel(BaseModel):
    """
    Define contrato para exibição dos filme em destaque na API do TMDB.
    """
    id: int = 1022789
    title: str = 'Divertida Mente 2'
    vote_average: float = 7.8
    release_date: str = '2024-06-11'
    poster_path: Optional[str] = 'https://'

class TMDBTrendingMoviesResultModel(BaseModel):
    """
    Define contrato para exibição dos filmes em destaque na API do TMDB.
    """
    page: int = 1
    total_pages: int
    total_results: int
    results: list[TMDBTrendingMoviesModel]