from pydantic import BaseModel
from typing import Optional

class BuscaPorTermoSchemaModel(BaseModel):
    """
    Define contrato para busca por termo
    """
    termo: str = "Marvel"
    idioma: str = "pt-BR"
    ano: Optional[int] = None
    pagina: int = 1

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