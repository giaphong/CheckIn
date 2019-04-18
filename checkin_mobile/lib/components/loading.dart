import 'package:flutter/material.dart';

class LoadingBuilder extends StatelessWidget {
  LoadingBuilder({this.text, this.color});

  final String text;
  final Color color ;

  @override
  Widget build(BuildContext context) {
    var bodyProgress = new Container(
      margin: const EdgeInsets.all(16.0),
      alignment: AlignmentDirectional.center,
      child: new Container(
        alignment: AlignmentDirectional.center,
        child: new Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            new CircularProgressIndicator(
              valueColor: new AlwaysStoppedAnimation<Color>(
                  color.withOpacity(0.9)),
              value: null,
              strokeWidth: 8.0,
            ),
            new Container(
              height: 10.0,
              child: new Text(' '),
            ),
            new Text(
              text ?? '',style: TextStyle(color: color, fontSize: 15.0),
            ),
          ],
        ),
      ),
    );
    return bodyProgress;
  }
}
