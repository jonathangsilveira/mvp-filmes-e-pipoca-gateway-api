from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, Response
from flask_cors import CORS
from requests import HTTPError
import json

from app import *

from app.response.json_response import JsonResponse

from app.mapper.mappers import to_result_model, to_movie_detais_model
from app.mapper.mappers import to_watchlist_model, to_trending_movies_model

info = Info(title="MVP Filmes e Pipoca Gateway API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

rate_tag = Tag(name='Avaliação de filmes', 
               description='Avaliar um filme atribuindo uma nota de 0 a 10')
watchlist_tag = Tag(name='Lista para assistir depois', 
                    description='Adição, remoção e visualização de lista com filmes.')
search_tag = Tag(name='Busca de filmes', 
                 description='Busca de filmes por termo')
trendings_tag = Tag(name='Filmes em alta', 
                    description='Lista os filmes em alta pela janela de tempo')

@app.route('/api')
def swagger_doc():
    """
    Redireciona para visualização do estilo de documentação Swagger.
    """
    return redirect('/openapi/swagger')

@app.get(rule='/api/movie', tags=[watchlist_tag], 
         responses={200: MovieDetailsModel, 400: ErrorModel, 404: ErrorModel})
def get_movie_details(query: MovieDetailsQuerySchema) -> Response:
    """
    Retorna detalhes do filme passado no parâmetro do query.
    """
    try:
        details = get_details(
            api_key=TMDB_API_KEY, 
            movie_id=query.movie_id, 
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
    
@app.get(rule='/api/search/movie', tags=[search_tag], 
         responses={200: MovieSearchResultsModel, 400: ErrorModel, 404: ErrorModel})
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

@app.post(rule='/api/watchlist/create', tags=[watchlist_tag], 
          responses={200: models.WatchlistCreatedModel, 400: ErrorModel})
def post_create_watchlist() -> Response:
    """
    Rota que cria uma nova lista de interesse.
    """
    try:
        watchlist_created = WatchlistController.create()
        return JsonResponse.make_json_response(
            model=watchlist_created
        )
    except Exception as e:
        return JsonResponse.make_error_response(
            message=f'Não foi possível criar uma nova lista de interesse!', 
            code=400
        )

@app.get(rule='/api/watchlist', tags=[watchlist_tag], 
         responses={200: WatchlistModel, 400: ErrorModel})
def get_watchlist(query: GetWatchlistQueryModel) -> Response:
    """
    Rota que cria uma nova lista de interesse.
    """
    try:
        watchlist = WatchlistController.get(query.watchlist_id)
        movies = []
        for movie_id in watchlist.movie_ids:
            detail = get_details(
                api_key=TMDB_API_KEY, 
                movie_id=movie_id, 
                language=query.language
            )
            movies.append(detail)
        return JsonResponse.make_json_response(
            model=to_watchlist_model(
                tmdb_models=movies, 
                watchlist_id=watchlist.watchlist_id
            )
        )
    except Exception as e:
        return JsonResponse.make_error_response(
            message=f'Não foi possível criar uma nova lista de interesse!', 
            code=400
        )
    
@app.post(rule='/api/watchlist/add', tags=[watchlist_tag], 
          responses={200: SuccessModel, 400: ErrorModel})
def post_add_movie(body: AddMovieToWatchlistBodyModel) -> Response:
    """
    Rota para adicionar um filme para dada lista de interesse.
    """
    try:
        success = WatchlistController.add_movie(body.watchlist_id, body.movie_id)
        return JsonResponse.make_json_response(
            model=success
        )
    except Exception:
        return JsonResponse.make_error_response(
            message=f'Não foi possível criar uma nova lista de interesse!', 
            code=400
        )
    
@app.delete(rule='/api/watchlist/remove', tags=[watchlist_tag], 
            responses={200: SuccessModel, 400: ErrorModel})
def delete_remove_movie(body: RemoveMovieToWatchlistBodyModel) -> Response:
    """
    Rota para adicionar um filme para dada lista de interesse.
    """
    try:
        success = WatchlistController.remove_movie(body.watchlist_id, body.movie_id)
        return JsonResponse.make_json_response(
            model=success
        )
    except Exception:
        return JsonResponse.make_error_response(
            message=f'Não foi possível criar uma nova lista de interesse!', 
            code=400
        )
    
@app.put(rule='/api/movie/rate', tags=[rate_tag], 
         responses={200: SuccessModel, 400: ErrorModel})
def put_rate_movie(body: RateMovieBodyModel) -> Response:
    """
    Rota para fornecer uma avaliação para filmes.
    """
    try:
        result = rate_movie(
            movie_id=body.movie_id, 
            rate_value=body.rate_value
        )
        return JsonResponse.make_json_response(
            model=result
        )
    except Exception:
        return JsonResponse.make_error_response(
            message=f'Não foi avaliar o filme {body.movie_id}', 
            code=400
        )
    
@app.get(rule='/api/trending/movies', tags=[trendings_tag], 
         responses={200: TrendingMoviesModel, 400: ErrorModel})
def get_trendings(query: GetTrendingMoviesQueryModel) -> Response:
    """
    Rota para lista os filmes em alta dado um período de tempo.
    """
    try:
        results = get_trending_movies(
            api_key=TMDB_API_KEY,
            language=query.language,
            time_window=query.time_window
        )
        trendings = to_trending_movies_model(results)
        return JsonResponse.make_json_response(
            model=trendings
        )
    except Exception:
        return JsonResponse.make_error_response(
            message=f'Não foi possível listas os filmes em alta para janela de tempo {query.time_window}', 
            code=400
        )