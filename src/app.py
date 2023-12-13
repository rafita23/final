from flask import Flask 
from config import config

#reoutes
from routes import movie

app=Flask(__name__)

def page_not_found(error):
    return "<h1>NO ENCONTRADO RAFA </h1>", 404
if __name__=='__main__':
    app.config.from_object(config['development'])


    #blueprints
    app.register_blueprint(movie.main, url_prefix='/api/movies')

    app.register_error_handler(404, page_not_found)
    app.run()
