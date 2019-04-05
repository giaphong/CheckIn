import 'package:flutter/material.dart';

class About extends StatelessWidget {
  @override
  Widget build(BuildContext context) => new Scaffold(
        //App Bar
        appBar: new AppBar(
          centerTitle: true,
          backgroundColor: Colors.redAccent,
          title: new Text(
            'About',
            style: new TextStyle(
              fontSize: 17.0,
            ),
          ),
          elevation: 2.0,
        ),

        //Content of tabs
        body: new PageView(
          children: <Widget>[
            new Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[new Text('About page content')],
            )
          ],
        ),
      );
}
