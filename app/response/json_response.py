from pydantic import BaseModel
from flask import Response

from app.schemas.schema_models import SuccessModel, ErrorModel

JSON_MIMETYPE = 'application/json'

class JsonResponse(object):
    
    @staticmethod
    def make_json_response(model: BaseModel, code: int = 200) -> Response:
        """
        Produz uma resposta padrão de erro no formato JSON.

        Parâmetros:
            model: Modelo que será convertido em JSON.
            code: Código HTTP de erro.
        """
        return Response(
            mimetype=JSON_MIMETYPE,
            status=code,
            response=model.model_dump_json(exclude_unset=True)
        )

    @staticmethod
    def make_success_response(message: str) -> Response:
        """
        Produz uma resposta padrão de sucesso no formato JSON.

        Parâmetro:
            message: Mensagem de sucesso.
        """
        success = SuccessModel(message=message)
        return JsonResponse.make_json_response(model=success)

    @staticmethod
    def make_error_response(message: str, code: int) -> Response:
        """
        Produz uma resposta padrão de erro no formato JSON.

        Parâmetro:
            message: Mensagem de sucesso.
            code: Código HTTP de erro.
        """
        error = ErrorModel(error_massage=message)
        return JsonResponse.make_json_response(
            model=error,
            code=code
        )
