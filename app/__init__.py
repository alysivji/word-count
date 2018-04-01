from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

# create and config app
app = Flask(__name__)
app.config.from_object(Config)

# set up plugins
bootstrap = Bootstrap(app)

from app import routes  # noqa
