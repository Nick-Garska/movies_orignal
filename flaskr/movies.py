from flask import Blueprint, request, render_template
from flaskr.db import find_by_id, get_movies

bp = Blueprint('movies', __name__, url_prefix='/movies')

@bp.route('/', methods=['GET'])
def movie_list():
    args= request.args
    if 'id' in args:
        movie_id =args['id']
        movies=find_by_id(movie_id)
        return render_template('movie_by_id.html', movies=movies)

    movies = get_movies()
    return render_template('movies.html', movies=movies)