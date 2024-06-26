

from app.tmdb.model.tmdb_search_result_model import TMDBMovieSearchResultsModel, TMDBMovieSearchResultModel
from app.tmdb.model.tmdb_movie_details_model import TMDBGenreModel, TMDBMovieDetailsModel
from app.schemas.schema_models import MovieSearchResultsModel, MovieSearchResultModel
from app.schemas.schema_models import GenreModel, MovieDetailsModel
from app.tmdb.config import TMDB_IMAGE_URL

def to_result_model(tmdb_model: TMDBMovieSearchResultsModel) -> MovieSearchResultsModel:
    return MovieSearchResultsModel(
        page=tmdb_model.page,
        total_pages=tmdb_model.total_pages,
        total_results=tmdb_model.total_results,
        results=[to_movie_model(result) for result in tmdb_model.results]
    )

def to_movie_model(tmdb_model: TMDBMovieSearchResultModel) -> MovieSearchResultModel:
    return MovieSearchResultModel(
        movie_id=tmdb_model.id,
        original_title=tmdb_model.original_title,
        title=tmdb_model.title,
        release_date=tmdb_model.release_date,
        poster_path=f'{TMDB_IMAGE_URL}{tmdb_model.poster_path}',
        overview=f'{tmdb_model.overview[:197]} ...'
    )

def to_genre_model(tmdb_model: TMDBGenreModel) -> GenreModel:
    """
    Mapeia modelo da resposta da API TMDB para gêneros em modelo de resposta.

    Parâmetro:
        tmdb_model: Modelo de resposta da API externa.
    """
    return GenreModel(
        id=tmdb_model.id, 
        name=tmdb_model.name
    )

def to_movie_detais_model(tmdb_model: TMDBMovieDetailsModel) -> MovieDetailsModel:
    """
    Mapeia modelo da resposta da API TMDB para detalhes do filme em modelo de resposta.

    Parâmetro:
        tmdb_model: Modelo de resposta da API externa.
    """
    return MovieDetailsModel(
        id=tmdb_model.id,
        title=tmdb_model.title,
        original_title=tmdb_model.original_title,
        original_language=tmdb_model.original_language,
        budget=tmdb_model.budget,
        backdrop_path=f'{TMDB_IMAGE_URL}{tmdb_model.backdrop_path}',
        poster_path=f'{TMDB_IMAGE_URL}{tmdb_model.poster_path}',
        genres=[to_genre_model(genre) for genre in tmdb_model.genres],
        overview=tmdb_model.overview,
        release_date=tmdb_model.release_date,
        revenue=tmdb_model.revenue,
        runtime='{}h {}min'.format(*divmod(tmdb_model.runtime, 60)),
        status=tmdb_model.status,
        tagline=tmdb_model.tagline
    )