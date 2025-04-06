class ReminderCard extends StatelessWidget {
  final String title;
  ReminderCard({required this.title});

  @override
  Widget build(BuildContext context) {
    return Card(child: ListTile(title: Text(title)));
  }
}
