import 'package:flutter/material.dart';

class Support extends StatelessWidget {
  @override
  Widget build(BuildContext context) => new Scaffold(
        //App Bar
        appBar: new AppBar(
          centerTitle: true,
          backgroundColor: Colors.redAccent,
          title: new Text(
            'Support',
            style: new TextStyle(
              fontSize: 20.0,
            ),
          ),
          elevation: 4.0,
        ),

        //Content of tabs
        body: new PageView(
          children: <Widget>[
            new Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                new Text('Support page content'),
              ],
            )
          ],
        ),
      );
}
