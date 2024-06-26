from typing import Optional
from pydantic import BaseModel

class TMDBErrorModel(BaseModel):
    """
    Modelo que representa uma resposta de erro da API TMDB.
    """

    success: bool
    status_code: Optional[int] = None
    status_message: Optional[str] = None