from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.items import Item


class CountryList(Resource):
    @jwt_required()
    def get(self):
        return {'countries': list(map(lambda x: x.json(), Item.query.all()))}


class Capital(Resource):
    def get(self,name):
        item=Item.get_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404


    def post(self,name):
        parser = reqparse.RequestParser()
        parser.add_argument('capital',
                            type=str,
                            required=True
                            )
        request_data = parser.parse_args()
        new_country = Item(name,request_data['capital'])
        try:
            new_country.insert()
        except:
            return {"message": "An error occurred inserting the item"}, 500
        return new_country.json(),201


    def delete(self, name):
        item = Item.get_by_name(name)
        if item:
            item.delete()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 404





