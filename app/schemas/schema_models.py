from pydantic import BaseModel, field_validator
from typing import Optional

class MovieSearchSchemaModel(BaseModel):
    """
    Define contrato para busca de filmes por termo
    """
    query: str = "Marvel"
    language: str = "pt-BR"
    year: Optional[int] = None
    page: int = 1

class MovieDetailsQuerySchema(BaseModel):
    """
    Define contrato para exibir detalhes do filme.
    """
    language: str = "pt-BR"

class MovieDetailsPathSchema(BaseModel):
    """
    Define contrato para parâmetro do path da requisição de detalhes do filme.

    Parâmetros:
        movie_id: ID do filme.
    """
    movie_id: int = 1022789

class TrendingMoviesModel(BaseModel):
    """
    Define contrato para exibição dos filmes em destaque.
    """
    movie_id: int = 1022789
    title: str = 'Divertida Mente 2'
    vote_average: int = 78
    release_date: str = '2024-06-11'
    poster_path: Optional[str] = 'https://'

class MovieSearchResultModel(BaseModel):
    """
    Define contrato para exibição dos resultados da pesquisa por filmes.
    """
    id: int = 1022789
    original_title: str = 'Inside Out 2'
    title: str = 'Divertidamente 2'
    release_date: str = '2024-06-11'
    overview: str = 'Divertida Mente 2, da Disney e Pixar, volta a entrar na mente da agora adolescente Riley, no momento ...'
    vote_average: int = 78
    poster_path: Optional[str] = 'https://'

class MovieSearchResultsModel(BaseModel):
    """
    Define contrato para exibição dos resultados da pesquisa por filmes.
    """
    page: int = 1
    total_pages: int = 13
    total_results: int = 253
    results: list[MovieSearchResultModel] = []

class GenreModel(BaseModel):
    """
    Define contrato para exibição de gêneros de filmes.
    """
    id: int = 16
    name: str = 'Animação'

class MovieDetailsModel(BaseModel):
    """
    Define contrato para exibição dos detalhes do filme.
    """
    id: int = 1022789
    title: str = 'Divertida Mente 2'
    original_title: str = 'Inside Out 2'
    budget: int = 200000000
    release_date: str = '2024-06-11'
    runtime: str = '1h 40min'
    overview: str = 'Divertida Mente 2, da Disney e Pixar, volta a entrar na mente da agora adolescente Riley, ...'
    backdrop_path: str = '.../image.jpg'
    poster_path: str = '.../image.jpg'
    original_language: str = 'en'
    tagline: str = 'Grandes mudanças. Novas emoções.'
    revenue: int = 728993234
    status: str = 'Lançado'
    vote_average: int = 78
    genres: list[GenreModel] = []

class GetWatchlistQueryModel(BaseModel):
    """
    Define contrato para parâmetro de consulta de lista de interesses. 
    """
    watchlist_id: int = 1
    language: str = 'pt-BR'

class WatchlistMovieModel(BaseModel):
    """
    Define contrato para exibição do filme que compoe a lista de interesses.
    """
    id: int = 1022789
    original_title: str = 'Inside Out 2'
    title: str = 'Divertidamente 2'
    release_date: str = '2024-06-11'
    overview: str = 'Divertida Mente 2, da Disney e Pixar, volta a entrar na mente da agora adolescente Riley, no momento ...'
    vote_average: int = 78
    poster_path: Optional[str] = 'https://'

class WatchlistModel(BaseModel):
    """
    Define contrato para parâmetro de consulta de lista de interesses. 
    """
    id: int = 1
    movies: list[WatchlistMovieModel] = []

class AddMovieToWatchlistPathModel(BaseModel):
    """
    Define contrato para parâmetro do path da requisição de adicionar filmes para lista de interesses.
    """
    watchlist_id: int = 1
    movie_id: int = 1022789

class RemoveMovieToWatchlistPathModel(BaseModel):
    """
    Define contrato para parâmetro do path da requisição de remover filmes da lista de interesses.
    """
    watchlist_id: int = 1
    movie_id: int = 1022789

class RateMovieBodyModel(BaseModel):
    """
    Define contrato para exibição avaliação de filmes.

    Parâmetros:
        movie_id: ID do filme.
        rate_value: Valor entre 0 e 10 para avaliação fo filme.
    """
    movie_id: int = 1022789
    rate_value: int = 9

    @field_validator('rate_value')
    @classmethod
    def validate_rate_value(cls, v: int) -> int:
        # Valida se rate_value está entre 0 e 10.
        if v > 10 and v < 0:
            raise ValueError('Nota da avaliação deve ser entre 0 e 10!')
        return v

class SuccessModel(BaseModel):
    """
    Define contrato para exibição de resultado de sucesso padrão.
    """
    message: str = 'Operação concluída com sucesso!'

class ErrorModel(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    error_massage: str = "Erro ao adicionar filme na watchlist!"