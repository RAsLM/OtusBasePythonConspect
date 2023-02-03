import os

from flask import Flask
from flask_migrate import Migrate
from werkzeug.exceptions import InternalServerError
from werkzeug.exceptions import HTTPException
from views.products import products_app
from models import db

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")

# app.config.update(
#     SQLALCHEMY_TRACK_MODIFICATIONS=False,
#     SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://user:password@localhost:5432/shop"
# )

CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)
migrate = Migrate(app, db)


# with app.app_context():
#     db.create_all()

@app.route("/")
def root():
    return "<h1>Hell<!h1>"

# @app.before_request
#
# @app.after_request

@app.route("/items/")
@app.route("/items/<int:item_id>/")
def get_item(item_id = None):
    return {"item_id": item_id}

@app.errorhandler(KeyError)
def handle_key_error(exc):
    if isinstance(exc, HTTPException):
        return exc
    print("exc", exc)
    return InternalServerError("oops, could not find that!")

@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(exc):
    print("exc", exc)
    return InternalServerError("oops, could divide that!")

# @app.errorhandler(Exception)
# def handle_all_exception(exc):
#     print("exc", exc)
#     return InternalServerError("oops, unexpected error!")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
