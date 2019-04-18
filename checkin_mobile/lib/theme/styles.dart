import 'package:flutter/material.dart';

ExactAssetImage logo = new ExactAssetImage("icon/logo.png");

TextStyle logoutTextStyle = new TextStyle(
  color: whiteColor,
  fontSize: 16.0,
  fontWeight: FontWeight.bold,
);

TextStyle usernameTextStyle = new TextStyle(
  color: whiteColor,
  fontSize: 16.0,
  fontWeight: FontWeight.bold,
);

TextStyle emailTextStyle = new TextStyle(
  color: whiteColor,
  fontSize: 16.0,
  fontWeight: FontWeight.bold,
);

TextStyle qtyStyle = const TextStyle(
  fontSize: 21.0,
  color: secondaryColor,
  fontWeight: FontWeight.bold,
);
TextStyle todoQtyStyle = new TextStyle(
  fontSize: 21.0,
  color: highlightColor,
  fontWeight: FontWeight.bold,
);
TextStyle noteStyle = const TextStyle(
  fontSize: 14.0,
  color: primaryColor,
);

TextStyle primaryTextStyle = new TextStyle(
  color: primaryColor,
);
TextStyle primaryBoldTextStyle = new TextStyle(
  color: primaryColor,
  fontWeight: FontWeight.bold,
);
TextStyle primaryI14TextStyle = const TextStyle(
  color: primaryColor,
  fontSize: 14.0,
  fontStyle: FontStyle.italic,
);
TextStyle primaryI18TextStyle = const TextStyle(
  color: primaryColor,
  fontSize: 18.0,
  fontStyle: FontStyle.italic,
);
TextStyle primary14TextStyle = const TextStyle(
  color: primaryColor,
  fontSize: 14.0,
);
TextStyle primary18TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 18.0,
);
TextStyle primaryBold18TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 18.0,
  fontWeight: FontWeight.bold,
);
TextStyle primary24TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 24.0,
);
TextStyle primaryBold24TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 24.0,
  fontWeight: FontWeight.bold,
);
TextStyle primaryBold32TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 32.0,
  fontWeight: FontWeight.bold,
);
TextStyle primaryBold36TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 36.0,
  fontWeight: FontWeight.bold,
);
TextStyle primary36TextStyle = new TextStyle(
  color: primaryColor,
  fontSize: 36.0,
);
TextStyle whiteTextStyle = const TextStyle(
  color: whiteColor,
);
TextStyle white12TextStyle = const TextStyle(
  color: whiteColor,
  fontSize: 12.0,
);
TextStyle white14TextStyle = const TextStyle(
  color: whiteColor,
  fontSize: 14.0,
);
TextStyle white18TextStyle = const TextStyle(
  color: whiteColor,
  fontSize: 18.0,
);
TextStyle white24TextStyle = const TextStyle(
  color: whiteColor,
  fontSize: 24.0,
);
TextStyle white32TextStyle = const TextStyle(
  color: whiteColor,
  fontSize: 32.0,
);
TextStyle secondaryTextStyle = new TextStyle(
  color: secondaryColor,
);
TextStyle secondary14TextStyle = new TextStyle(
  color: secondaryColor,
  fontSize: 14.0,
);
TextStyle secondary18TextStyle = new TextStyle(
  color: secondaryColor,
  fontSize: 18.0,
);
TextStyle background24TextStyle = new TextStyle(
  color: backgroundColor,
  fontSize: 24.0,
);
TextStyle error18TextStyle = new TextStyle(color: errorColor, fontSize: 18.0);

BoxDecoration badgeBorderBox = new BoxDecoration(
    color: whiteColor,
    borderRadius: borderRadiusCircular5,
    border: new Border.all(
      color: secondaryColor,
    ));

Radius circular5 = const Radius.circular(5.0);
BorderRadius borderRadiusCircular5 = new BorderRadius.all(circular5);
BorderRadius borderRadiusCircularTop5 =
    new BorderRadius.only(topLeft: circular5, topRight: circular5);
BorderRadius borderRadiusCircularBottom5 =
    new BorderRadius.only(bottomLeft: circular5, bottomRight: circular5);

final ThemeData appTheme = new ThemeData(
  primaryColor: primaryColor,
  iconTheme: new IconThemeData(color: whiteColor),
  primaryColorBrightness: Brightness.dark,
  backgroundColor: transparentColor,
  indicatorColor: whiteColor,
  accentColorBrightness: Brightness.dark,
  accentColor: whiteColor,
  brightness: Brightness.light,
);
const Color whiteColor = const Color(0XFFFFFFFF);
const Color primaryColor = const Color(0xFF14346a);
const Color backgroundColor = const Color(0xFFD0D6E3);
const Color secondaryColor = const Color(0xFF8999b4);
const Color highlightColor = const Color(0xFFFF6F00);
const Color errorColor = const Color(0xFFEB313E);
const Color successColor = const Color(0xFF4CAF50);
Image miniLogo = new Image(
    image: new ExactAssetImage("assets/header-logo.png"),
    height: 28.0,
    width: 123.5,
    alignment: FractionalOffset.center);

const Color transparentColor = const Color.fromRGBO(0, 0, 0, 0.2);

class GoBackRoute<T> extends MaterialPageRoute<T> {
  GoBackRoute({WidgetBuilder builder, RouteSettings settings})
      : super(builder: builder, settings: settings);

  @override
  Widget buildTransitions(BuildContext context, Animation<double> animation,
      Animation<double> secondaryAnimation, Widget child) {
    return child;
  }
}

final ShapeBorder shape = new RoundedRectangleBorder(
    borderRadius: new BorderRadius.only(
  topLeft: circular5,
  topRight: circular5,
  bottomLeft: circular5,
  bottomRight: circular5,
));
