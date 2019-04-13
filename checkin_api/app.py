import flask
from flask import request, jsonify
import requests , json


app = flask.Flask(__name__)


@app.route('/api/v1/user/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    URL_LOGIN = 'http://127.0.0.1:8069/api/user/get_token';

    params = {
        'login': email,
        'password':password
    }
    if params is not None:
        URL_LOGIN += '?'
    for key in params:
        URL_LOGIN += key+'='+params[key]+'&'

    response = requests.get(URL_LOGIN)
    return response.text



@app.route('/api/v1/user/checkin', methods=['POST'])
def checkIn():
    URL_CHECKIN = 'http://127.0.0.1:8069/api/mobile.checkin/create';

    timestamp = request.json['timestamp']
    lat = request.json['lat']
    lng = request.json['lng']
    photo = request.json['photo']
    token = request.json['token']
    params = {
        'timestamp': timestamp,
        'lat': lat,
        'lng': lng,
        'photo': photo,
    }
    requestBodyArray = {
        'token': token,
        'create_vals': params
    }
    requestBodyForm = {'params': requestBodyArray}
    requestBody = json.dumps(requestBodyForm)

    headers = {}
    headers['Content-Type'] = "application/json";
    response = requests.post(URL_CHECKIN, data=requestBody, headers= headers)
    return response.text



if __name__ == '__main__':
    app.run()
