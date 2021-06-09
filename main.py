from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return jsonify({'test': 'dkljkjn;sgv;ms'})

api.add_resource(Test, '/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)