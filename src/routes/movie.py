from flask import Blueprint, jsonify, request
from models.entities.Movie import Movie
from models.MovieModel import MovieModel



main= Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/<id>')
def get_movie(id):
     try:
        movie = MovieModel.get_movie(id)
        if movie != None:
             return jsonify(movie)
        else:
             return jsonify({}), 404
     except Exception as ex:
         return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_movie():
     try:
       identificador=request.json['id']
       nombre=request.json['nombre']
       apellido=request.json['apellido']
       direccion=request.json['direccion']

       movie=Movie(identificador,nombre,apellido,direccion)
       affected_rows=MovieModel.add_movie(movie)

       if affected_rows == 1:
            return jsonify(movie.id)
       else:
            return jsonify({'message': "error rafa"}),500
       return jsonify({})
     except Exception as ex:
         return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
     try:
       
       nombre=request.json['nombre']
       apellido=request.json['apellido']
       direccion=request.json['direccion']

       movie=Movie(id,nombre,apellido,direccion)
       affected_rows=MovieModel.update_movie(movie)

       if affected_rows == 1:
            return jsonify(movie.id)
       else:
            return jsonify({'message': "error rafa"}),500
       return jsonify({})
     except Exception as ex:
         return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
     try:
       movie=Movie(id)

       affected_rows=MovieModel.delete_movie(movie)
       if affected_rows == 1:
            return jsonify(movie.id)
       else:
            return jsonify({'message': "error rafa"}),500
       return jsonify({})
     except Exception as ex:
         return jsonify({'message': str(ex)}), 500
