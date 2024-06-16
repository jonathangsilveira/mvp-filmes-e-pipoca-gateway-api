from typing import Optional
from pydantic import BaseModel

from app.tmdb.model.genre_model import GenreModel

class MovieSearchModel(BaseModel):
    """
    Modelo representando as informações do filme obtido como resultado de busca na API do TMDB.
    """

    id: int
    title: str
    popularity: float
    vote_average: float
    poster_path: Optional[str] = None
    release_date: Optional[str] = None
    runtime: Optional[int] = None
    genres: Optional[list[GenreModel]] = None