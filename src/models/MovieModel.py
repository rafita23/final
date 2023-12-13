from database.db import get_connection
from .entities.Movie import Movie

class MovieModel ():
    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id,nombre,apellido,direccion FROM cliente ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movies.append(movie.to_JSON())
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def get_movie(self,id):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("SELECT id,nombre,apellido,direccion FROM cliente WHERE id= %s",(id,))
                row= cursor.fetchone()
                
                movie=None
                if row != None:
                    movie = Movie(row[0], row[1], row[2], row[3])
                    movie= (movie.to_JSON())
            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_movie(self,cliente):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO cliente (id,nombre,apellido,direccion) 
                VALUES (%s, %s, %s, %s)""",(cliente.id,cliente.nombre,cliente.apellido,cliente.direccion))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_movie(self,cliente):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE cliente SET nombre = %s, apellido=%s, direccion=%s 
                WHERE id=%s""", (cliente.nombre,cliente.apellido,cliente.direccion,cliente.id))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
   
    @classmethod
    def delete_movie(self,cliente):
        try:
            connection = get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM cliente where id= %s",(cliente.id))
                affected_rows=cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

