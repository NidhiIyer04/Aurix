class AssistantProvider with ChangeNotifier {
  String _suggestion = "Take a break!";
  String get suggestion => _suggestion;

  void updateSuggestion(String newOne) {
    _suggestion = newOne;
    notifyListeners();
  }
}
