from flask import Blueprint
from ..jobs import public as public_jb

public_bp = Blueprint('public', __name__)

@public_bp.route("/")
def home(): return public_jb.home()

@public_bp.route("/favicon.ico")
def favicon(): return public_jb.favicon()