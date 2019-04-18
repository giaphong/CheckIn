import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_demo/components/flushbar.dart';
import 'package:image_demo/components/loading.dart';
import 'package:image_demo/model/checkin.dart';
import 'package:image_demo/model/photo.dart';
import 'package:image_demo/screens/list_checkin.dart';
import 'package:image_demo/screens/login.dart';
import 'package:image_demo/theme/styles.dart';
import 'package:image_demo/utils/globle.dart';
import 'package:image_picker/image_picker.dart';
import 'package:location/location.dart';

class MyHomePage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return new MyHomePageState();
  }
}

class MyHomePageState extends State<MyHomePage> {
  File _image;
  LocationData currentLocation;

  Location _locationService = new Location();
  bool _permission = false;
  String error;
  double opacity = 1.0;

  Future getImage() async {
    var image = await ImagePicker.pickImage(
        source: ImageSource.camera, maxWidth: 480.0, maxHeight: 480.0);

    setState(() {
      _image = image;
    });
    checkInServer();
  }

  initPlatformState() async {
    LocationData location;
    await _locationService.changeSettings(
        accuracy: LocationAccuracy.HIGH, interval: 1000);

    try {
      bool serviceStatus = await _locationService.serviceEnabled();
      if (serviceStatus) {
        _permission = await _locationService.requestPermission();
        if (_permission) {
          location = await _locationService.getLocation();
          setState(() {
            currentLocation = location;
          });
        }
      } else {
        bool serviceStatusResult = await _locationService.requestService();
        if (serviceStatusResult) {
          initPlatformState();
        }
      }
    } catch (e) {
      print(e);
      if (e.code == 'PERMISSION_DENIED') {
        error = e.message;
      } else if (e.code == 'SERVICE_STATUS_ERROR') {
        error = e.message;
      }
      location = null;
    }
  }

  void showToast(String title, String content, IconData icon, int seconds) {
    Container(
      margin: EdgeInsets.only(top: 100.0),
      child: Flushbar(
        flushbarPosition: FlushbarPosition.TOP,
        flushbarStyle: FlushbarStyle.FLOATING,
        reverseAnimationCurve: Curves.decelerate,
        forwardAnimationCurve: Curves.elasticOut,
        backgroundColor: Colors.white,
        isDismissible: false,
        duration: Duration(seconds: seconds),
        icon: Icon(
          icon,
          color: primaryColor,
          size: 30.0,
        ),
        mainButton: FlatButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          child: Text(
            "Ẩn",
            style: TextStyle(
                color: primaryColor,
                fontWeight: FontWeight.bold,
                fontSize: 20.0),
          ),
        ),
        titleText: Text(
          title,
          style: TextStyle(
              color: primaryColor, fontSize: 20.0, fontWeight: FontWeight.bold),
        ),
        messageText: Text(
          content,
          style: TextStyle(color: primaryColor, fontSize: 15.0),
        ),
      )..show(context),
    );
  }

  @override
  void initState() {
    super.initState();
    initPlatformState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Giao diện checkin'),
          centerTitle: true,
        ),
        drawer: SafeArea(
          child: Drawer(
            child: Column(
              children: <Widget>[
                new UserAccountsDrawerHeader(
                  decoration: BoxDecoration(color: primaryColor),
                  accountEmail: new Text(
                    userGlobal.email,
                    style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 20.0),
                  ),
                  currentAccountPicture: new Container(
                      width: 48.0,
                      height: 48.0,
                      child: Image.asset('assets/avatar.png'),
                      decoration: new BoxDecoration(
                        shape: BoxShape.circle,
                      )),
                  margin: EdgeInsets.zero,
                  onDetailsPressed: () {},
                ),
                new ListTile(
                    title: new Text(
                      "Danh sách checkin",
                      style: TextStyle(
                          color: primaryColor,
                          fontSize: 20.0,
                          fontWeight: FontWeight.bold),
                    ),
                    trailing: new Icon(Icons.arrow_right),
                    onTap: () {
                      Navigator.of(context).push(
                        MaterialPageRoute(
                            builder: (context) => LoadScreenListCheckIn()),
                      );
                    }),
                Spacer(),
                new ListTile(
                    title: new Text(
                      "Thoát ứng dụng",
                      style: TextStyle(
                          color: primaryColor,
                          fontSize: 20.0,
                          fontWeight: FontWeight.bold),
                    ),
                    trailing: new Icon(Icons.arrow_right),
                    onTap: () {
                      Navigator.pushAndRemoveUntil(
                          context,
                          MaterialPageRoute(builder: (context) => LoginPage()),
                          ModalRoute.withName("/"));
                    }),
              ],
            ),
          ),
        ),
        body: opacity == 0
            ? LoadingBuilder(
                text: 'Đang gửi dữ liệu...',
                color: primaryColor,
              )
            : Column(
                children: <Widget>[
                  new GestureDetector(
                    child: new Container(
                      padding: EdgeInsets.all(20.0),
                      height: MediaQuery.of(context).size.height * 3 / 5,
                      width: MediaQuery.of(context).size.width,
                      child: _image == null
                          ? new Stack(
                              children: <Widget>[
                                new Center(
                                  child: new CircleAvatar(
                                    radius: 80.0,
                                    backgroundColor: const Color(0xFF778899),
                                  ),
                                ),
                                new Center(
                                  child: new Image.asset(
                                    "assets/camera.png",
                                  ),
                                ),
                              ],
                            )
                          : new Container(
                              child: Image.asset(_image.path),
                            ),
                    ),
                    onTap: () {
                      getImage();
                    },
                  ),

//                  new Container(
//                    width: MediaQuery.of(context).size.width,
//                    height: 50,
//                    margin: EdgeInsets.all(20.0),
//                    child: new FlatButton(
//                      child: Text(
//                        "Báo cáo sự cố",
//                        textAlign: TextAlign.center,
//                        style: TextStyle(
//                            color: Colors.white, fontWeight: FontWeight.bold),
//                      ),
//                      shape: new RoundedRectangleBorder(
//                        borderRadius: new BorderRadius.circular(30.0),
//                      ),
//                      color: primaryColor,
//                      onPressed: () {
////                        checkInServer();
//                      },
//                    ),
//                  ),
                ],
              ));
  }

  void checkInServer() {
    setState(() {
      opacity = 0.0;
    });
    if (_image != null) {
      if (currentLocation.longitude != null) {
        upload(_image, true, API_KEY, API_SECRET, BASE_URL).then((value) {
          print(new DateTime.now().toString());
          if (value != '') {
            CheckIn checkin = new CheckIn(
                datetime: new DateTime.now().toString(),
                lat: currentLocation.latitude,
                lng: currentLocation.longitude,
                urlImage: value);

            checkIn(checkin).then((value) {
              if (value) {
                showToast("Checkin Thành công", "Cảm ơn bạn nhá",
                    Icons.account_circle, 3);
              } else {
                showToast("Checkin Thất bại", "Vui lòng thử lại",
                    Icons.account_circle, 3);
              }
            });
          } else {
            showToast("Checkin Thất bại", "Vui lòng thử lại",
                Icons.account_circle, 3);
          }
          setState(() {
            opacity = 1.0;
            _image = null;
          });
        });
      } else {
        showToast("Bạn chưa bật vị trí", "Vui lòng mở vị trí của bạn ",
            Icons.account_circle, 3);
        setState(() {
          opacity = 1.0;
          _image = null;
        });
      }
    } else {
      showToast("Bạn chưa chọn ảnh", "Vui lòng chụp ảnh trước đã.",
          Icons.account_circle, 3);
      setState(() {
        opacity = 1.0;
        _image = null;
      });
    }
  }
}
