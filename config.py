"""Flask configuration variables."""
import os
import dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# dotenv.load_dotenv(os.path.join(basedir, '.env'))

dotenv.load_dotenv()


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False