from requests import post, get, delete, Response

from app.data.config import config

from app.data.model import models

from app.schemas.schema_models import SuccessModel, ErrorModel

class WatchlistController(object):
    """
    Implementação de acesso as funcionalidades de manipulação da lista.
    """

    @staticmethod
    def create() -> models.WatchlistCreatedModel:
        """
        Cria uma nova lista de interesse.
        """
        response: Response = post(
            url=f'{config.DATA_API_BASE_URL}/watchlist/create'
        )
        response.raise_for_status()
        body = response.json()
        return models.WatchlistCreatedModel(**body)
    
    @staticmethod
    def get(watchlist_id: int) -> models.WatchlistModel:
        """
        Recupera uma lista de interesse pelo ID.

        Parâmetros:
            watchlist_id: ID da lista de interesse.
        """
        query_params = {'watchlist_id': watchlist_id}
        response: Response = get(
            url=f'{config.DATA_API_BASE_URL}/watchlist',
            params=query_params
        )
        response.raise_for_status()
        body = response.json()
        return models.WatchlistModel(**body)
    
    @staticmethod
    def add_movie(watchlist_id: int, movie_id: int) -> SuccessModel:
        """
        Recupera uma lista de interesse pelo ID.

        Parâmetros:
            watchlist_id: ID da lista de interesse.
        """
        response: Response = post(
            url=f'{config.DATA_API_BASE_URL}/watchlist/{watchlist_id}/add/{movie_id}'
        )
        response.raise_for_status()
        body = response.json()
        return SuccessModel(**body)
    
    @staticmethod
    def remove_movie(watchlist_id: int, movie_id: int) -> SuccessModel:
        """
        Recupera uma lista de interesse pelo ID.

        Parâmetros:
            watchlist_id: ID da lista de interesse.
        """
        response: Response = delete(
            url=f'{config.DATA_API_BASE_URL}/watchlist/{watchlist_id}/remove/{movie_id}'
        )
        response.raise_for_status()
        body = response.json()
        return SuccessModel(**body)
