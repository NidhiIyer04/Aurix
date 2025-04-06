class TaskCard extends StatelessWidget {
  final String title;
  final List<String> steps;
  TaskCard({required this.title, required this.steps});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          Text(title),
          ...steps.map((s) => Text("- $s")),
        ],
      ),
    );
  }
}
