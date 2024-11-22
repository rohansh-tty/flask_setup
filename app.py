from flask import Flask
import logging
import config
import api
from flask_restful import Resource, Api
import time
from flask import jsonify
from flask_restful import Api, Resource
from tasks import celery
import config

from models import db
import os 

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object('config')
    db.init_app(app)

    # define hello world page


    @app.route('/')
    def hello_world():
        return 'Hello, World!'


    

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)