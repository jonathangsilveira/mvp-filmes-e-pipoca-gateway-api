from typing import Optional

class ErrorModel:
    """
    Modelo que representa uma resposta de erro da API TMDB.
    """

    success: bool
    status_code: Optional[int] = None
    status_message: Optional[str] = None