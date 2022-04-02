from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class status(Resource):
    def get(self):
        try:
            return {'data': 'Hello! Welcome to api based Calculator.'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}

class Sum(Resource):
    def get(self, a, b):
        return jsonify({'sum': a+b})

class Subtract(Resource):
    def get(self, a, b):
        if a>b:
            result = {"subtract":a-b}
            return jsonify(result)
        elif a<b:
            result = {"subtract":b-a}
            return jsonify(result)
        else:
            result = {"subtract":a-b}
            return jsonify(result)

class Multiply(Resource):
    def get(self, a, b):
        return jsonify({'product': a*b})

class Divide(Resource):
    def get(self, a, b):

        return jsonify({'quotient': a/b})


api.add_resource(status, '/')
api.add_resource(Sum, '/sum/<int:a>,<int:b>')
api.add_resource(Subtract, '/subtract/<int:a>,<int:b>')
api.add_resource(Multiply, '/multiply/<int:a>,<int:b>')
api.add_resource(Divide, '/divide/<int:a>,<int:b>')

if __name__ == '__main__':
    app.run()