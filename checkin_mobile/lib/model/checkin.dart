import 'package:http/http.dart';

class CheckIn {
  String username;
  String datetime;
//   new DateTime.now().toIso8601String();
  double lat;
  double lng;
  String urlImage;

  CheckIn({this.username, this.datetime, this.lat, this.lng, this.urlImage});

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data["username"] = this.username;
    data["datetime"] = this.datetime;
    data["lat"] = this.lat;
    data["lng"] = this.lng;
    data["urlImage"] = this.urlImage;

    return data;
  }

  factory CheckIn.fromJson(Map<String, dynamic> json) {
    return CheckIn(
      username: json['username'],
      datetime: json['datetime'],
      lat: json['lat'],
      lng: json['lng'],
      urlImage: json['urlImage'],
    );
  }
}

Future<String> sendCheckin(String url, String body) async {
  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
//  headers['Authorization'] = token;
  var response = await post(url, body: body, headers: headers);
  String res = response.body;
  return 'OK';
}
