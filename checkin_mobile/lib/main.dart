import 'package:image_demo/app_config.dart';
import 'package:image_demo/screens/login.dart';
import 'package:flutter/material.dart';
import 'package:image_demo/theme/styles.dart';
import 'package:package_info/package_info.dart';

class DwtApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {

    return new MaterialApp(
      debugShowCheckedModeBanner: false,
      home: new LoginPage(),
      theme: appTheme,
    );
  }
}

void main() async {
  PackageInfo packageInfo = await PackageInfo.fromPlatform();
  String version = packageInfo.version;
  var configuredApp = new AppConfig(
    appName: 'DNP Water Alpha',
    flavorName: 'dev',
    appVersion: version,
    child: new DwtApp(),
  );

  runApp(configuredApp);
}

