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

class MovieDetailsSchemaModel(BaseModel):
    """
    Define contrato para exibir detalhes do filme.
    """
    movie_id: int = 250
    language: str = "pt-BR"

class ErrorSchemaModel(BaseModel):
    """
    Define contrato para exibir resposta de erro.
    """
    reason: str