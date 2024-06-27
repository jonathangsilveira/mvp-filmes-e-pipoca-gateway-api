from typing import Optional
from pydantic import BaseModel

from app.tmdb.model.tmdb_genre_model import TMDBGenreModel

class TMDBMovieDetailsModel(BaseModel):
    """
    Modelo representando os detalhes do filme obtidos na API do TMDB.
    """

    id: int
    original_language: str
    original_title: str
    title: str
    revenue: int
    vote_average: float
    overview: Optional[str] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None
    release_date: Optional[str] = None
    runtime: Optional[int] = None
    status: Optional[str] = None
    tagline: Optional[str] = None
    budget: Optional[int] = None
    genres: Optional[list[TMDBGenreModel]] = None
    homepage: Optional[str] = None
    imdb_id: Optional[str] = None