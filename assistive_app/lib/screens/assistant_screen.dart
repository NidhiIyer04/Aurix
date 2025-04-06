class AssistantScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Assistant')),
      body: ReminderCard(title: 'Stretch break at 3 PM'),
    );
  }
}
