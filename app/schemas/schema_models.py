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

class ErrorSchemaModel(BaseModel):
    """
    Define contrato para exibir resposta de erro.
    """
    reason: str