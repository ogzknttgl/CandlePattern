#create a flask rest api and get input from user about timestamp and pattern type and send it to the flask server and get the response


#create a flask rest api and get input from user about timestamp and pattern type and send it to the flask server and get the response
import requests
import json
import pandas as pd
import ast
import numpy as np
import datetime
from flask_restful import Resource, Api, reqparse
from flask import Flask, request


app = Flask(__name__)
api = Api(app)

class Ratio(Resource):
    def get(self):
        begin = 1535932800000
        timestamp = int(request.args.get('timestamp'))
        pattern = (request.args.get('pattern'))
        pattern = [int(i) for i in pattern]
        data = pd.read_csv('candle_30m_new.csv')
        count = 0
        g = 0
        r = 0
        current_time = int((((timestamp - begin) / 18) / 100000))
        length_pattern = len(pattern)
        for i in range (0, current_time):
            for n in range(0, length_pattern):
                if data['number'][n] == pattern[n]:
                    count += 1
                    if  data['number'][length_pattern + 1 ] == 1:
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

api.add_resource(Ratio, '/Ratio')

if __name__ == '__main__':
    app.run()



