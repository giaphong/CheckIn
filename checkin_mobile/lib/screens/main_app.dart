import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_demo/components/flushbar.dart';
import 'package:image_demo/model/checkin.dart';
import 'package:image_demo/model/photo.dart';
import 'package:image_demo/screens/about.dart';
import 'package:image_demo/screens/support.dart';
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
    var image = await ImagePicker.pickImage(source: ImageSource.camera);

    setState(() {
      _image = image;
    });
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
          color: Colors.redAccent,
          size: 30.0,
        ),
        mainButton: FlatButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          child: Text(
            "Ẩn",
            style: TextStyle(
                color: Colors.redAccent,
                fontWeight: FontWeight.bold,
                fontSize: 20.0),
          ),
        ),
        titleText: Text(
          title,
          style: TextStyle(
              color: Colors.redAccent,
              fontSize: 20.0,
              fontWeight: FontWeight.bold),
        ),
        messageText: Text(
          content,
          style: TextStyle(color: Colors.redAccent, fontSize: 15.0),
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
          title: Text('Home'),
          backgroundColor: Colors.redAccent,
          centerTitle: true,
        ),
        drawer: SafeArea(
          child: Drawer(
            child: Column(
              children: <Widget>[
                new UserAccountsDrawerHeader(
                  accountName: new Text(userGlobal.name,
                      style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 20.0)),
                  decoration: BoxDecoration(color: Colors.redAccent),
                  accountEmail: new Text(
                    userGlobal.email,
                    style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 15.0),
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
                    title: new Text("About"),
                    trailing: new Icon(Icons.arrow_right),
                    onTap: () {
                      Navigator.of(context).pop();
                      Navigator.of(context).push(new MaterialPageRoute(
                          builder: (BuildContext context) => new About()));
                    }),
                new Divider(),
                new ListTile(
                    title: new Text("Support"),
                    trailing: new Icon(Icons.arrow_right),
                    onTap: () {
                      Navigator.of(context).pop();
                      Navigator.of(context).push(new MaterialPageRoute(
                          builder: (BuildContext context) => new Support()));
                    }),
                new Divider(),
              ],
            ),
          ),
        ),
        body: Column(
          children: <Widget>[
            new GestureDetector(
              child: new Container(
                height: MediaQuery.of(context).size.height / 2,
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
            new Container(
              width: MediaQuery.of(context).size.width,
              margin: const EdgeInsets.only(left: 30.0, right: 30.0, top: 20.0),
              alignment: Alignment.center,
              child: new Row(
                children: <Widget>[
                  new Expanded(
                      child: Opacity(
                    child: new FlatButton(
                      shape: new RoundedRectangleBorder(
                        borderRadius: new BorderRadius.circular(30.0),
                      ),
                      color: Colors.redAccent,
                      onPressed: () {
                        setState(() {
                          opacity = 0.0;
                        });
                        if (_image != null) {
                          if (currentLocation.longitude != null) {
                            print(currentLocation.latitude);
                            print(currentLocation.longitude);
                            upload(_image, true, API_KEY, API_SECRET, BASE_URL)
                                .then((value) {
                              print('Nguyen Gia Phong:' + value);
                              CheckIn checkin = new CheckIn();
                              setState(() {
                                opacity = 1.0;
                              });
                            });
                          }
                        } else {
                          showToast(
                              "Bạn chưa chọn ảnh",
                              "Vui lòng chụp ảnh trước đã.",
                              Icons.account_circle,
                              3);
                        }
                      },
                      child: new Container(
                        padding: const EdgeInsets.symmetric(
                          vertical: 20.0,
                          horizontal: 20.0,
                        ),
                        child: new Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: <Widget>[
                            new Expanded(
                              child: Text(
                                "Check In",
                                textAlign: TextAlign.center,
                                style: TextStyle(
                                    color: Colors.white,
                                    fontWeight: FontWeight.bold),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    opacity: opacity,
                  )),
                ],
              ),
            ),
          ],
        ));
  }
}
