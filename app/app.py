from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS
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
            response=json.dumps({
                'id': details.id, 
                'title': details.title, 
                'original_language': details.original_language,
                'popularity': details.popularity,
                'vote_average': details.vote_average,
                'vote_count': details.vote_count,
                'overview': details.overview,
                'poster_path': f'{TMDB_IMAGE_URL}/{details.poster_path}',
                'backdrop_path': f'{TMDB_IMAGE_URL}/{details.backdrop_path}',
                'release_date': details.release_date,
                'runtime': details.runtime,
                'status': details.status, 
                'genres': [genre.name for genre in details.genres]}),
            status=200,
            mimetype='application/json'
        )
    except TMDBException as tmdb:
        return make_error_response(
            message=f'Erro ao chamar serviço externo: {tmdb.status_code} - {tmdb.status_messagem}', 
            code=404
        )
    except Exception as cause:
        return make_error_response(
            message=f'Não foi possível retornar os detalhos do id {query.movie_id}', 
            code=404
        )
    
@app.get('/api/search/movie')
def get_search_movies(query: MovieSearchSchemaModel) -> Response:
    """
    Busca por filmes contendo o termo pesquisado e ano de lançamento (opcional).
    """
    try:
        page = search_movies(api_key=TMDB_API_KEY, query=query.query, 
                                language=query.language, page=query.page, 
                                year=query.year)
        movies: list[MovieSearchModel] = []
        for movie in page.results:
            movies.append(
                movie.model_copy(
                    update={'poster_path': f'{TMDB_IMAGE_URL}/{movie.poster_path}'}
                )
            )
        copied_page = page.model_copy(update={'results': movies})
        return Response(
            response=copied_page.model_dump_json(exclude_unset=True),
            status=200,
            mimetype='application/json'
        )
    except TMDBException as tmdb:
        return make_error_response(
            message=f'Erro ao chamar serviço externo: {tmdb.status_code} - {tmdb.status_messagem}', 
            code=404
        )
    except Exception as cause:
        return make_error_response(
            message=f'Não foi possível retornar resultados para o termo buscado: {query.query}', 
            code=400
        )
    
def make_error_response(message: str, code: int) -> Response:
    """
    Produz uma resposta no formato JSON.
    """
    return Response(response=json.dumps({'error_message': message}), status=code, 
                    mimetype='application/json')