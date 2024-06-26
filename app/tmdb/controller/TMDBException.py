from requests import Response
from typing import Optional

from app.tmdb.model.tmdb_error_model import TMDBErrorModel

class TMDBException(Exception):
    """
    Exceção lançada quando a reposta da API do TMDB for de falha.
    """
    
    status_code: Optional[int]
    status_messagem: Optional[str]

    def __init__(self, *args: object, 
                 status_code: Optional[int] = None, status_messagem: Optional[str] = None) -> None:
        """
        Parâmetros:
            status_code: Código de erro da API do TMDB.
            status_message: Mensagem de erro da API do TMDB.
        """
        super().__init__(*args)
        self.status_code = status_code
        self.status_messagem = status_messagem

def raise_for_tmdb_error(response: Response) -> None:
    """
    Valida se o retorno da requisição a API do TMDB é de erro para lançar a exceção TMDBException.
    """
    if response.ok:
        return
    body = response.json()
    model = TMDBErrorModel(**body)
    raise TMDBException(
        status_code=model.status_code, 
        status_messagem=model.status_message
    )
        