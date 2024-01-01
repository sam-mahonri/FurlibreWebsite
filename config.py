from dotenv import load_dotenv
import os
from datetime import timedelta
from flask_limiter.util import get_remote_address

load_dotenv()

class Config:
    
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV')
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

    LIMITER_ENABLED = True
    LIMITER_STORAGE_URI = "memory://"
    LIMITER_KEY_FUNC = get_remote_address
    
    MONGO_URI = os.getenv('MONGO_URI')
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = os.getenv('MONGO_PORT')
    MONGO_DBNAME =os.getenv('MONGO_DBNAME')
    MONGO_USERNAME = os.getenv('MONGO_USERNAME')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
    
    SESSION_COOKIE_HTTPONLY=True
    SESSION_COOKIE_SAMESITE='Strict'
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_NAME = 'access_token_cookie'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES')))
    JWT_COOKIE_SAMESITE = 'Strict'
    JWT_COOKIE_HTTPONLY = True
    JWT_CSRF_CHECK_FORM = True
    JWT_COOKIE_CSRF_PROTECT = False
    
    BABEL_DEFAULT_LOCALE = 'en'
    LANGUAGES = ['en', 'es', 'pt_BR']
    BABEL_DOMAINS = ['buttons', 'errors']

