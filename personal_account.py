from flask import jsonify
from flask_restful import Resource
from flask_login import current_user

class Account():
    def get(self):
        return