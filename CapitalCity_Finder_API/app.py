from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.items import CountryList,Capital
from resources.user import Register
from security import authenticate,identity
from db import db


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = '#1234#'


api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(CountryList, '/countries')
api.add_resource(Capital, '/capital/<string:name>')
api.add_resource(Register, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)