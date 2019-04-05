import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


class User():
    def __init__(self, email , password, name):
        self.email = email
        self.password = password
        self.name = name




class CheckIn():
    def __init__(self, name , timestamp , lat, lng , photo ):
        self.name = name
        self.timestamp = timestamp
        self.lat = lat
        self.lng = lng
        self.photo = photo


listUser = []
listUser.append(User('phongng52@wru.vn', '12345', 'Nguyen Van A'))
listUser.append(User('phongng51@wru.vn', '12345', 'Nguyen Van B'))
listUser.append(User('phongng50@wru.vn', '12345', 'Nguyen Van C'))
listUser.append(User('phongng49@wru.vn', '12345', 'Nguyen Van D'))


@app.route('/api/v1/user/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    for user in  listUser:
        if user.email == email and user.password == password:
            us = {'email': user.email,'name': user.name }
            return jsonify(us);
    response = jsonify({'message': u'Email hoặc mật khẩu không đúng'})
    return response, 401



@app.route('/api/v1/user/checkin', methods=['POST'])
def checkIn():
    email = request.json['name']
    password = request.json['timestamp']
    lat = request.json['lat']
    lng = request.json['lng']
    photo = request.json['photo']
    return jsonify('HI')



if __name__ == '__main__':
    app.run()