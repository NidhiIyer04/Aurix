class TaskManagerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Task Manager')),
      body: TaskCard(title: "Take meds", steps: ["Open bottle", "Drink water"]),
    );
  }
}
