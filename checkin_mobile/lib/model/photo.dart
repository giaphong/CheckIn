import 'dart:convert';
import 'package:crypto/crypto.dart';
import 'package:http/http.dart';
import 'package:image/image.dart' as Img;

class Photo {
  String url;

  Photo({this.url});

  factory Photo.fromJson(Map<String, dynamic> json) {
    return Photo(
      url: json['url'],
    );
  }
}

Future<String> upload(_image, compress, apiKey, apiSecret, BASE_URL) async {
  List<int> imageBytes = _image.readAsBytesSync();
  if (compress) {
    Img.Image image = Img.decodeImage(imageBytes);
    Img.Image thumbnail = Img.copyResize(image, 480);
    imageBytes = Img.encodeJpg(thumbnail);
  }
  String base64Image = base64.encode(imageBytes);
  int timestamp = new DateTime.now().millisecondsSinceEpoch;
  Map params = {
    'api_key': apiKey,
    'file': 'data:image/png;base64,' + base64Image,
    'timestamp': timestamp.toString(),
  };
  Map<String, String> plainMap = new Map<String, String>.from(params);
  plainMap.remove('api_key');
  plainMap.remove('file');
  var plainList = new List<String>();
  plainMap.forEach((key, value) {
    plainList.add(key + '=' + value);
  });
  String plainText = plainList.join("&") + apiSecret;
  params['signature'] = sha1.convert(utf8.encode(plainText)).toString();
  String requestBody = json.encode(params);

  Map<String, String> headers = {};
  headers['Content-Type'] = "application/json";
  headers['Authorization'] = 'ddae9b93be2640b6acb788fe6384862c';
  var response = await post(BASE_URL, headers: headers, body: requestBody);
  Map<String, dynamic> map = json.decode(response.body);
  Photo photo = Photo.fromJson(map);

  return photo.url;
}
