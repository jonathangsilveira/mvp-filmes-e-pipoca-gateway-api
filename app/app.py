from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response, jsonify
from flask_cors import CORS
from typing import Optional
import json

from app import *

info = Info(title="MVP The Movie Database Gateway API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

@app.route('/api')
def documentacao_swagger():
    """Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.get('/api/movie')
def get_movie_details(query: MovieDetailsSchemaModel):
    """
    Retorna detalhes do filme.
    """
    try:
        details = get_details(api_key=TMDB_API_KEY, movie_id=query.movie_id, 
                              language=query.language)
        return Response(
            response=json.dumps({'id': details.id, 
                                 'title': details.title, 
                                 'genres': [genre.name for genre in details.genres] 
            }),
            status=200,
            mimetype='application/json'
        )
    except Exception as cause:
        return make_error_response(
            message=f'Não foi possível retornar os detalhos do id {query.movie_id}', 
            code=404
        ) 
    
def make_error_response(message: str, code: int) -> Response:
    """
    Produz uma resposta no formato JSON.
    """
    return Response(response=json.dumps({'error_message': message}), status=code, 
                    mimetype='application/json')