from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flaskapp.django_query import DjangoQuery

db = SQLAlchemy(query_class=DjangoQuery)
migrate = Migrate()
