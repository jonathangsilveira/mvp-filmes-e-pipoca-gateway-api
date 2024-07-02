from pydantic import BaseModel
from typing import Optional

class TMDBTrendingMoviesModel(BaseModel):
    """
    Define contrato para exibição dos filmes em destaque na API do TMDB.
    """
    id: int = 1022789
    title: str = 'Divertida Mente 2'
    vote_average: int = 78
    release_date: str = '2024-06-11'
    poster_path: Optional[str] = 'https://'