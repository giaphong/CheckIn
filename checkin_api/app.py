import flask
from flask import request, jsonify
import requests, json
import jwt
import os

app = flask.Flask(__name__)

URL = os.environ.get('URL', 'http://127.0.0.1:8069/')


@app.route('/api/v1/user/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    URL_LOGIN = URL + 'api/user/get_token';
    print(URL_LOGIN)
    params = {
        'login': email,
        'password': password
    }
    if params is not None:
        URL_LOGIN += '?'
    for key in params:
        URL_LOGIN += key + '=' + params[key] + '&'

    response = requests.get(URL_LOGIN)
    data = json.loads(response.text)
    result = data['success']
    try:
        print(result['token'])
        payload = {
            'token': result['token'],
            'uid': result['uid']
        }
        token = jwt.encode(
            payload,
            'SECRET_KEY',
            algorithm='HS256'
        );

        res = {'token': token.decode('unicode_escape')}
        return jsonify(res)
    except Exception as e:
        return e


@app.route('/api/v1/user/checkin', methods=['POST'])
def checkIn():
    URL_CHECKIN = URL + 'api/mobile.checkin/create';

    timestamp = request.json['timestamp']
    lat = request.json['lat']
    lng = request.json['lng']
    photo = request.json['photo']
    token = request.headers.get("Authorization")

    payload_data = jwt.decode(token, 'SECRET_KEY', algorithms="HS256")
    user_id = payload_data['uid']
    token_odoo = payload_data['token']

    params = {
        'timestamp': timestamp,
        'lat': lat,
        'lng': lng,
        'photo': photo,
        'user_id': user_id
    }
    requestBodyArray = {
        'token': token_odoo,
        'create_vals': params
    }
    requestBodyForm = {'params': requestBodyArray}
    requestBody = json.dumps(requestBodyForm)

    headers = {}
    headers['Content-Type'] = "application/json";
    response = requests.post(URL_CHECKIN, data=requestBody, headers=headers)

    return response.text


@app.route('/api/v1/user/getlistcheckin', methods=['GET'])
def getListCheckIn():
    URL_LIST_CHECKIN = URL + "api/mobile.checkin/method/get_checkin?"
    URL_LIST_ID = URL + 'api/mobile.checkin/search?'

    token = request.headers.get("Authorization")
    payload_data = jwt.decode(token, 'SECRET_KEY', algorithms="HS256")
    token_odoo = payload_data['token']

    URL_LIST_ID = URL_LIST_ID + "token=" + token_odoo
    responseIDs = requests.get(URL_LIST_ID)
    jsonids = json.loads(responseIDs.text)
    listIds = '[ '
    for id in jsonids:
        strid = id['id']
        listIds = listIds + str(strid) + ', '
    listIds = listIds + ' ]'

    URL_LIST_CHECKIN = URL_LIST_CHECKIN + "token=" + token_odoo + "&ids=" + listIds
    responseListCheck = requests.get(URL_LIST_CHECKIN)
    jsonData = json.loads(responseListCheck.text)
    try:
        listCheckIn = jsonData['success']
        return jsonify(listCheckIn)
    except Exception as e:
        return ''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
