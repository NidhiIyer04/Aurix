class ChatScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Chat')),
      body: ChatBubble(message: "Hello!", isSentByUser: true),
    );
  }
}
