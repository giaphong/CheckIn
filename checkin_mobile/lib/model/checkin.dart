import 'dart:convert';

import 'package:http/http.dart';
import 'package:image_demo/utils/globle.dart';

class CheckIn {
  String datetime;
  double lat;
  double lng;
  String urlImage;
  String token;

  CheckIn({this.datetime, this.lat, this.lng, this.urlImage, this.token});

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data["timestamp"] = this.datetime;
    data["lat"] = this.lat;
    data["lng"] = this.lng;
    data["photo"] = this.urlImage;
    data['token'] = this.token;
    return data;
  }
}



Future<int> checkIn(CheckIn checkin) async {
  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
  var response = await post(URL_CHECKIN_FLASK,
      body: json.encode(checkin.toJson()), headers: headers);
  Map<String, dynamic> map = json.decode(response.body);
  Result result = Result.fromJson(map);
  Map<String, dynamic> map1 = json.decode(result.result);
  Result result1 = Result.fromJson(map1);
  return result1.id;
}

class Result {
  String result;
  int id;
  String token;

  Result({this.result, this.id, this.token});

  factory Result.fromJson(Map<String, dynamic> json) {
    return Result(result: json['result'], id: json['id'], token: json['token']);
  }
}
