from flask import Flask, make_response, Response, request
from http import HTTPStatus
import json


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        users = {}
        @app.route("/user", methods=['POST'])
        def create_user() -> Response:
            data_string = request.get_data()
            try:
                user = user_from_json(data_string)
                name = user['name']
                users[name] = user
                return make_response({"data": f"User {name} is created!"}, HTTPStatus.CREATED)
            except KeyError as e:
                return make_response({"errors": e.args[0]}, HTTPStatus.UNPROCESSABLE_ENTITY)
                
        @app.route("/user/<username>", methods=['GET', 'PATCH', 'DELETE'])
        def user_actions(username) -> Response:
            if not username:
                return make_response('', HTTPStatus.NOT_FOUND)
            try:
                user = users[username]
            except KeyError:
                return make_response('', HTTPStatus.NOT_FOUND)
            
            def get_user() -> Response:
                user_name = user['name']
                return make_response({"data": f"My name is {user_name}"}, HTTPStatus.OK)
            
            def update_user() -> Response:
                data_string = request.get_data()
                try:
                    user = user_from_json(data_string)
                    users[username] = user
                    new_user_name = user['name']
                    return make_response({"data": f"My name is {new_user_name}"}, HTTPStatus.OK)
                except KeyError as e:
                    return make_response({"errors": e.args[0]}, HTTPStatus.UNPROCESSABLE_ENTITY)
            
            def delete_user() -> Response:
                del users[username]
                return make_response('', HTTPStatus.NO_CONTENT)
            
            match request.method:
                case 'GET':
                    return get_user()
                case 'PATCH':
                    return update_user()            
                case 'DELETE':
                    return delete_user()
                
        def user_from_json(data_string: str) -> dict:
            data = json.loads(data_string)
            if 'name' in data and isinstance(data['name'], str) and len(data['name']) > 0:
                return data
            raise KeyError({"name": "This field is required"})