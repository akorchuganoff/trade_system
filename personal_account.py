from flask import jsonify
from flask_restful import Resource
from flask_login import current_user


class Account(Resource):
    def get(self):
        return jsonify({'current_user': current_user.id})