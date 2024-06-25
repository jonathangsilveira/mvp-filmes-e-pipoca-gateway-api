from typing import Optional
from pydantic import BaseModel

from app.tmdb.model.tmdb_genre_model import TMDBGenreModel

class TMDBMovieSearchResultModel(BaseModel):
    """
    Modelo representando as informações do filme obtido como resultado de busca na API do TMDB.
    """

    id: int
    original_title: str
    title: str
    release_date: str
    overview: str
    poster_path: Optional[str] = None