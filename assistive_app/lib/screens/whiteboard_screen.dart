class WhiteboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Visual Board')),
      body: VisualBoardTile(label: 'Meeting Notes'),
    );
  }
}
