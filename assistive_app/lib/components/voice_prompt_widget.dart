class VoicePromptWidget extends StatelessWidget {
  final String prompt;
  VoicePromptWidget({required this.prompt});

  @override
  Widget build(BuildContext context) {
    return Row(children: [Icon(Icons.mic), Text(prompt)]);
  }
}
