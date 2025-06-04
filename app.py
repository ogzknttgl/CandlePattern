from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from analysis import calculate_ratio
app = Flask(__name__)
api = Api(app)

class candle_30m_new(Resource):

    def get(self):
        data = pd.read_csv('candle_30m_new.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    pass
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pattern', type=str, required=True, help='pattern cannot be blank')
        parser.add_argument('timestamp', type=str, required=True, help='timestamp cannot be blank')
        data = parser.parse_args()
        data = ast.literal_eval(data['pattern'])
        data = ast.literal_eval(data['timestamp'])
        data = candle_30m_new(data)
        return {'data': data}, 200  # return data and 200 OK code
    pass

class Calc(Resource):

    def get(self):
        data = pd.read_csv('candle_30m_new.csv')
        data = data.to_dict()
        highest_close = max(data['close'].values())
        return {'highest_close': highest_close}, 200
    pass
from flask import request


class Ratio(Resource):
    def get(self):
        timestamp = int(request.args.get('timestamp'))
        pattern = request.args.get('pattern')
        result = calculate_ratio(pattern, timestamp)
        return result, 200

api.add_resource(Calc, '/Calc')
api.add_resource(candle_30m_new, '/candle_30m_new')
api.add_resource(Ratio, '/Ratio')

if __name__ == '__main__':
    app.run()  # run our Flask app
