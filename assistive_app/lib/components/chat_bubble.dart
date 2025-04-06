class ChatBubble extends StatelessWidget {
  final String message;
  final bool isSentByUser;

  ChatBubble({required this.message, required this.isSentByUser});

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: isSentByUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        margin: EdgeInsets.all(8),
        padding: EdgeInsets.all(12),
        color: isSentByUser ? Colors.blue[100] : Colors.grey[300],
        child: Text(message),
      ),
    );
  }
}
