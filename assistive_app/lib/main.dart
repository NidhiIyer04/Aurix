void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Assistive App',
      theme: AppTheme.lightTheme,
      home: HomeScreen(),
    );
  }
}
