from pydantic import BaseModel

class WatchlistCreatedModel(BaseModel):
    """
    Define contrato para exibição da lista de interesse criada.

    Parâmetros:
        watchlist_id: ID da lista de interesse.
    """
    watchlist_id: int = 1

class WatchlistModel(BaseModel):
    """
    Define contrato para exibição de resultados da lista para interesse.

    Parâmetros:
        watchlist: ID da watchlist.
        movie_ids: Lista de IDs dos filmes registrados na lista para interesse.
    """
    watchlist_id: int
    movie_ids: list[int]

class ErrorModel(BaseModel):
    """
    Define contrato para exibição de erros da API.
    """
    error_massage: str = "Erro ao adicionar filme na lista de interesse!"