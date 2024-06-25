from pydantic import BaseModel
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
    Define contrato para parâmetro do path da requisição.

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
    movie_id: int = 1022789
    original_title: str = 'Inside Out 2'
    title: str = 'Divertidamente 2'
    release_date: str = '2024-06-11'
    overview: str = 'Divertida Mente 2, da Disney e Pixar, volta a entrar na mente da agora adolescente Riley, no momento ...'
    poster_path: Optional[str] = 'https://'

class MovieSearchResultsModel(BaseModel):
    """
    Define contrato para exibição dos resultados da pesquisa por filmes.
    """
    page: int = 1
    total_pages: int = 13
    total_results: int = 253
    results: list[MovieSearchResultModel] = []

class SuccessModel(BaseModel):
    """
    Define contraro para exibição de resultado de sucesso padrão.
    """
    message: str = 'Operação concluída com sucesso!'

class ErrorModel(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    error_massage: str = "Erro ao adicionar filme na watchlist!"