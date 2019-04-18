import 'package:flutter/material.dart';
import 'package:image_demo/components/loading.dart';
import 'package:image_demo/model/checkin.dart';
import 'package:image_demo/theme/styles.dart';
import 'package:timeline_list/timeline.dart';
import 'package:timeline_list/timeline_model.dart';
import 'package:intl/intl.dart';

class LoadScreenListCheckIn extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _LoadScreenListCheckInState();
  }
}

class _LoadScreenListCheckInState extends State<LoadScreenListCheckIn> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Danh sách CheckIn'),
        centerTitle: true,
        actions: <Widget>[],
      ),
      body: FutureBuilder(
          future: getListCheckIn(),
          builder: (context, snapshot) {
            if (snapshot.hasError) print(snapshot.error);
            return snapshot.hasData
                ? ListCheckIn(listCheckIn: snapshot.data)
                : new LoadingBuilder(
                    text: 'Loading ...',
                    color: primaryColor,
                  );
          }),
    );
  }
}

class ListCheckIn extends StatefulWidget {
  List<CheckIn> listCheckIn;

  ListCheckIn({this.listCheckIn});

  @override
  State<StatefulWidget> createState() {
    return new _ListCheckInState();
  }
}

class _ListCheckInState extends State<ListCheckIn> {
  final PageController pageController =
      PageController(initialPage: 1, keepPage: true);
  int pageIx = 1;
  var formattedDate = DateFormat('dd-MM-yyyy – hh:mm:ss');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: ListView.builder(
      shrinkWrap: true,
      itemCount: widget.listCheckIn.length,
      itemBuilder: (context, index) {
        return GestureDetector(
          child: Container(
            padding: EdgeInsets.all(10.0),
            child: Card(
              margin: EdgeInsets.symmetric(vertical: 16.0),
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(8.0)),
              clipBehavior: Clip.antiAlias,
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: <Widget>[
                    Container(
                      height: 200.0,
                      child: Image.network(
                          widget.listCheckIn.elementAt(index).urlImage),
                    ),
                    const SizedBox(
                      height: 8.0,
                    ),
                    const SizedBox(
                      height: 8.0,
                    ),
                    Text(
                      formattedDate.format(DateTime.parse(
                          widget.listCheckIn.elementAt(index).datetime)),
                      style: TextStyle(color: Colors.black, fontSize: 24.0),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(
                      height: 8.0,
                    ),
                  ],
                ),
              ),
            ),
          ),
        );
      },
    ));
  }
}
