from flask_restful import Resource,reqparse
from models.user import User


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('_id',
                            type=int,
                            required=True
                            )
        parser.add_argument('username',
                                type=str,
                                required=True
                                )
        parser.add_argument('password',
                                type=str,
                                required=True
                                )
        request_data = parser.parse_args()

        if User.get_by_username(request_data['username']):
            return {"message": "User with that username already exists."}, 400

        user=User(request_data['username'], request_data['password'])
        user.insert()
        return {'message': 'user registered'},201
