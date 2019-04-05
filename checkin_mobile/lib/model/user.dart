import 'dart:convert';

import 'package:http/http.dart';

class User {
  String email;
  String name;
  String password;
  String message;

  User({this.email, this.name, this.password, this.message});

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data["email"] = this.email;
    data["password"] = this.password;
    return data;
  }

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
        email: json['email'], name: json['name'], message: json['message']);
  }
}

Future<User> loginUser(String url, String body) async {
  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
//  headers['Authorization'] = token;
  var response = await post(url, body: body, headers: headers);
  String res = response.body;
  print(res);
  Map<String, dynamic> map = json.decode(res);
  User user = User.fromJson(map);
  return user;
}
