class VisualBoardTile extends StatelessWidget {
  final String label;
  VisualBoardTile({required this.label});

  @override
  Widget build(BuildContext context) {
    return Card(child: Center(child: Text(label)));
  }
}
