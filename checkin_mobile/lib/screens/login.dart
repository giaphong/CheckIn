import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:image_demo/components/flushbar.dart';
import 'package:image_demo/components/loading.dart';
import 'package:image_demo/model/user.dart';
import 'package:image_demo/screens/main_app.dart';
import 'package:image_demo/theme/styles.dart';
import 'package:image_demo/utils/globle.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => new _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _emailController = new TextEditingController();
  final TextEditingController _passwordController = new TextEditingController();
  double opacity = 1.0;

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

  Widget LoginPage() {
    return new Container(
      height: MediaQuery.of(context).size.height,
      decoration: BoxDecoration(
        color: primaryColor,
      ),
      child: new Column(
        children: <Widget>[
          Container(
            padding: EdgeInsets.all(50.0),
            child: Center(
                child: Container(
              height: 150.0,
              child: Image.asset(
                'assets/logo.png',
                color: Colors.white,
              ),
            )),
          ),
          new Row(
            children: <Widget>[
              new Expanded(
                child: new Padding(
                  padding: const EdgeInsets.only(left: 40.0),
                  child: new Text(
                    "Email",
                    style: TextStyle(color: Colors.white, fontSize: 18.0),
                  ),
                ),
              ),
            ],
          ),
          new Container(
            width: MediaQuery.of(context).size.width,
            margin: const EdgeInsets.only(left: 40.0, right: 40.0, top: 0.0),
            alignment: Alignment.center,
            decoration: BoxDecoration(
              border: Border(
                bottom: BorderSide(
                    color: Colors.white, width: 0.5, style: BorderStyle.solid),
              ),
            ),
            padding: const EdgeInsets.only(left: 0.0, right: 10.0),
            child: new Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                new Expanded(
                  child: TextField(
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24.0,
                    ),
                    controller: _emailController,
                    textAlign: TextAlign.left,
                    decoration: InputDecoration(
                      border: InputBorder.none,
                      hintStyle: TextStyle(color: Colors.grey),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Divider(
            height: 24.0,
          ),
          new Row(
            children: <Widget>[
              new Expanded(
                child: new Padding(
                  padding: const EdgeInsets.only(left: 40.0),
                  child: new Text(
                    "Mật khẩu",
                    style: TextStyle(color: Colors.white, fontSize: 18.0),
                  ),
                ),
              ),
            ],
          ),
          new Container(
            width: MediaQuery.of(context).size.width,
            margin: const EdgeInsets.only(left: 40.0, right: 40.0, top: 0.0),
            alignment: Alignment.center,
            decoration: BoxDecoration(
              border: Border(
                bottom: BorderSide(
                    color: Colors.white, width: 0.5, style: BorderStyle.solid),
              ),
            ),
            padding: const EdgeInsets.only(left: 0.0, right: 10.0),
            child: new Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                new Expanded(
                  child: TextField(
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24.0,
                    ),
                    controller: _passwordController,
                    obscureText: true,
                    textAlign: TextAlign.left,
                    decoration: InputDecoration(
                      border: InputBorder.none,
                      hintStyle: TextStyle(color: Colors.grey),
                    ),
                  ),
                ),
              ],
            ),
          ),
          Divider(
            height: 24.0,
          ),
          new Container(
            width: MediaQuery.of(context).size.width,
            margin: const EdgeInsets.only(left: 30.0, right: 30.0, top: 20.0),
            alignment: Alignment.center,
            child: new Row(
              children: <Widget>[
                new Expanded(
                  child: new FlatButton(
                    shape: new RoundedRectangleBorder(
                      borderRadius: new BorderRadius.circular(30.0),
                    ),
                    color: Colors.transparent,
                    onPressed: () => {login()},
                    child: new Container(
                      padding: const EdgeInsets.symmetric(
                        vertical: 20.0,
                        horizontal: 20.0,
                      ),
                      child: new Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          new Expanded(
                            child: Text("Đăng nhập",
                                textAlign: TextAlign.center,
                                style: white24TextStyle),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: primaryColor,
        body: opacity == 0
            ? LoadingBuilder(
                text: 'Đang đăng nhâp...',
                color: Colors.white,
              )
            : SingleChildScrollView(
                child: LoginPage(),
              ));
  }

  login() {
    setState(() {
      opacity = 0.0;
    });
    String email = _emailController.text;
    String password = _passwordController.text;
    if (email.trim() != null && password.trim().length > 1) {
      User user = new User(email: email, password: password);

      loginCheck(user).then((value) {
        if (value) {
          userGlobal = user;
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => MyHomePage(),
            ),
          );
        } else {
          showToast("Đăng nhập thất bại", "Bạn vui lòng kiểm tra lại.",
              Icons.account_circle, 3);
        }
        setState(() {
          opacity = 1.0;
        });
      });
    } else {
      showToast("Email hoặc mật khẩu quá ngắn", "Bạn vui lòng kiểm tra lại.",
          Icons.account_circle, 3);
      setState(() {
        opacity = 1.0;
      });
    }
  }
}
