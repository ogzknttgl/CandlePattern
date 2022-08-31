from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
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
        begin = 1535932800000
        timestamp = int(request.args.get('timestamp'))
        pattern = (request.args.get('pattern'))
        pattern = [int(i) for i in pattern]
        data = pd.read_csv('candle_30m_new.csv')
        # data = data.to_dict()
        # pattern = [1,1,1,0]
        count = 0
        g = 0
        r = 0
        current_time = int((((timestamp - begin) / 18) / 100000))
        length_pattern = len(pattern)
        """
        for index, value in data.iterrows():
            if value["current_time"] >= current_time:
                break
            else:
                if index >= length_pattern:
                    checksum = []
                    for i, v in enumerate(pattern.reverse()):
                        is_green = value["close"] - value["open"] >= 0
                        _is_green = True if v == 1 else False
                        if _is_green == is_green:
                            checksum.append(True)
                        else:
                            checksum.append(False)
                    if all(checksum):
                        count += 1
                        if value["number"] == 1:
                            g += 1
                        else:
                            r += 1
        pattern_saw = count
        green_num = g
        red_num = r
        ratio_green = (g / (r + g)) * 100
        ratio_red = (r / (r + g)) * 100
        return {'pattern_saw': pattern_saw, 'green_num': green_num, 'red_num': red_num,
                'ratio_green': ratio_green, 'ratio_red': ratio_red}, 200
    pass
    """

        for i in range(0,current_time):
            if len(pattern) == 4:
                if data['number'][i] == pattern[0] and data['number'][i + 1] == pattern[1] and data['number'][i + 2] == pattern[2] and data['number'][i + 3] == pattern[3]:
                    count += 1
                    if data['number'][i + 4] == 1:
                        g += 1
                    else:
                        r += 1
            elif len(pattern) == 5:
                if data['number'][i] == pattern[0] and data['number'][i + 1] == pattern[1] and data['number'][i + 2] == pattern[2] and data['number'][i + 3] == pattern[3] and data['number'][i + 4] == pattern[4]:
                    count += 1
                    if data['number'][i + 5] == 1:
                        g += 1
                    else:
                        r += 1
            elif len(pattern) == 6:
                if data['number'][i] == pattern[0] and data['number'][i + 1] == pattern[1] and data['number'][i + 2] == pattern[2] and data['number'][i + 3] == pattern[3] and data['number'][i + 4] == pattern[4] and data['number'][i + 5] == pattern[5]:
                    count += 1
                    if data['number'][i + 6] == 1:
                        g += 1
                    else:
                        r += 1
            elif len(pattern) == 7:
                if data['number'][i] == pattern[0] and data['number'][i + 1] == pattern[1] and data['number'][i + 2] == pattern[2] and data['number'][i + 3] == pattern[3] and data['number'][i + 4] == pattern[4] and data['number'][i + 5] == pattern[5] and data['number'][i + 6] == pattern[6]:
                    count += 1
                    if data['number'][i + 7] == 1:
                        g += 1
                    else:
                        r += 1
        pattern_saw = count
        green_num =  g
        red_num =  r
        ratio_green =  (g / (r + g)) * 100
        ratio_red =  (r / (r + g)) * 100
        return {'pattern_saw': pattern_saw, 'green_num': green_num, 'red_num': red_num, 'ratio_green':ratio_green, 'ratio_red':ratio_red}, 200
    pass

api.add_resource(Calc, '/Calc')
api.add_resource(candle_30m_new, '/candle_30m_new')
api.add_resource(Ratio, '/Ratio')

if __name__ == '__main__':
    app.run()  # run our Flask app
