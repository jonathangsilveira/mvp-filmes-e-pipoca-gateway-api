from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS
import json

from app import *

from app.response.json_response import JsonResponse

from app.mapper.mappers import to_result_model, to_movie_detais_model

info = Info(title="MVP Filmes e Pipoca Gateway API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

@app.route('/api')
def swagger_doc():
    """Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.get('/api/movie/<int:movie_id>')
def get_movie_details(path: MovieDetailsPathSchema, query: MovieDetailsQuerySchema):
    """
    Retorna detalhes do filme passado no parâmetro do path.
    """
    try:
        details = get_details(
            api_key=TMDB_API_KEY, 
            movie_id=path.movie_id, 
            language=query.language
        )
        return JsonResponse.make_json_response(
            model=to_movie_detais_model(details)
        )
    except TMDBException as tmdb:
        return JsonResponse.make_error_response(
            message=f'Erro ao chamar serviço externo: {tmdb.status_code} - {tmdb.status_messagem}', 
            code=404
        )
    except Exception as e:
        print(f'Error: {str(e)}')
        return JsonResponse.make_error_response(
            message=f'Não foi possível retornar os detalhos do id {path.movie_id}', 
            code=400
        )
    
@app.get('/api/search/movie')
def get_search_movies(query: MovieSearchSchemaModel) -> Response:
    """
    Busca por filmes contendo o termo pesquisado e ano de lançamento (opcional).
    """
    try:
        tmdb_result_page = search_movies(
            api_key=TMDB_API_KEY, 
            query=query.query, 
            language=query.language, 
            page=query.page, 
            year=query.year
        )
        search_result_page = to_result_model(tmdb_result_page)
        return JsonResponse.make_json_response(
            model=search_result_page
        )
    except TMDBException as tmdb:
        return JsonResponse.make_error_response(
            message=f'Erro ao chamar serviço externo: {tmdb.status_code} - {tmdb.status_messagem}', 
            code=404
        )
    except Exception:
        return JsonResponse.make_error_response(
            message=f'Não foi possível retornar resultados para o termo buscado: {query.query}', 
            code=400
        )
    