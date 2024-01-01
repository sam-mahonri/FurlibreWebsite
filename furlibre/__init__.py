from flask import Flask
from config import Config
from flask_cors import CORS
from flask_babel import Babel, _
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_limiter import Limiter

app = Flask(__name__)
app.config.from_object(Config)

limiter = Limiter(
    key_func=Config.LIMITER_KEY_FUNC,
    storage_uri=Config.LIMITER_STORAGE_URI,
    app=app,
    default_limits=["120 per minute", "1 per second"]
    )

CORS(app)
babel = Babel(app)

def create_app():
        
    from .src.blueprints.public import public_bp
    
    app.register_blueprint(public_bp)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)
    
    return app