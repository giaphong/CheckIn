import 'dart:convert';
import 'package:queries/collections.dart';
import 'package:http/http.dart';
import 'package:image_demo/utils/globle.dart';

class CheckIn {
  String datetime;
  double lat;
  double lng;
  String urlImage;

  CheckIn({this.datetime, this.lat, this.lng, this.urlImage});

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data["timestamp"] = this.datetime;
    data["lat"] = this.lat;
    data["lng"] = this.lng;
    data["photo"] = this.urlImage;
    return data;
  }

  factory CheckIn.fromJson(Map<String, dynamic> json) {
    return CheckIn(
        datetime: json['timestamp'],
        lat: json['lat'],
        lng: json['lng'],
        urlImage: json['photo']);
  }
}

Future<bool> checkIn(CheckIn checkin) async {
  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
  headers['Authorization'] = TOKEN;
  try {
    var response = await post(URL_CHECKIN,
        body: json.encode(checkin.toJson()), headers: headers);
    Map<String, dynamic> map = json.decode(response.body);
    Result result = Result.fromJson(map);
    print(result.result);
    if (result.result.contains("success")) {
      return true;
    }
    return false;
  } catch (Ex) {
    return false;
  }
}

Future<List<CheckIn>> getListCheckIn() async {
  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
  headers['Authorization'] = TOKEN;
  var response = await get(URL_GET_LIST_CHECKIN, headers: headers);
  try{
    List responseJson = json.decode(response.body);
    List<CheckIn> list =
    responseJson.map((m) => new CheckIn.fromJson(m)).toList();
    return list.reversed.toList();
  }catch(ex){
    return null;
  }
}

class Result {
  String result;
  int id;
  String token;
  String success;

  Result({this.result, this.id, this.token, this.success});

  factory Result.fromJson(Map<String, dynamic> json) {
    return Result(
        result: json['result'],
        id: json['id'],
        token: json['token'],
        success: json['success']);
  }
}
