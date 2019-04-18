import 'dart:convert';

import 'package:http/http.dart';
import 'package:image_demo/utils/globle.dart';

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

Future<bool> loginCheck(User user1) async {
  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
  try {
    var response = await post(URL_LOGIN,
        body: json.encode(user1.toJson()), headers: headers);
    print(response.body);
    Map<String, dynamic> map = json.decode(response.body);
    Result result = Result.fromJson(map);
    if (result != null) {
      TOKEN = result.token;
      print(TOKEN);
      return true;
    } else
      return false;
  } catch (Ex) {
    return false;
  }
}

class Result {
  String token;

  Result({this.token});

  factory Result.fromJson(Map<String, dynamic> json) {
    return Result(token: json['token']);
  }
}
