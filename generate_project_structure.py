import os

BASE_DIR = "assistive_app/lib"

# Define the folder structure and file contents
files_structure = {
    "main.dart": """void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Assistive App',
      theme: AppTheme.lightTheme,
      home: HomeScreen(),
    );
  }
}
""",
    "screens/home_screen.dart": """class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Welcome')),
      body: Center(child: Text('Dashboard')),
    );
  }
}
""",
    "screens/task_manager_screen.dart": """class TaskManagerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Task Manager')),
      body: TaskCard(title: "Take meds", steps: ["Open bottle", "Drink water"]),
    );
  }
}
""",
    "screens/chat_screen.dart": """class ChatScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Chat')),
      body: ChatBubble(message: "Hello!", isSentByUser: true),
    );
  }
}
""",
    "screens/assistant_screen.dart": """class AssistantScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Assistant')),
      body: ReminderCard(title: 'Stretch break at 3 PM'),
    );
  }
}
""",
    "screens/whiteboard_screen.dart": """class WhiteboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Visual Board')),
      body: VisualBoardTile(label: 'Meeting Notes'),
    );
  }
}
""",
    "screens/settings_screen.dart": """class SettingsScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Settings')),
      body: Center(child: Text('Settings Options')),
    );
  }
}
""",
    "components/task_card.dart": """class TaskCard extends StatelessWidget {
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
""",
    "components/custom_button.dart": """class CustomButton extends StatelessWidget {
  final String label;
  final VoidCallback onPressed;

  CustomButton({required this.label, required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(onPressed: onPressed, child: Text(label));
  }
}
""",
    "components/voice_prompt_widget.dart": """class VoicePromptWidget extends StatelessWidget {
  final String prompt;
  VoicePromptWidget({required this.prompt});

  @override
  Widget build(BuildContext context) {
    return Row(children: [Icon(Icons.mic), Text(prompt)]);
  }
}
""",
    "components/reminder_card.dart": """class ReminderCard extends StatelessWidget {
  final String title;
  ReminderCard({required this.title});

  @override
  Widget build(BuildContext context) {
    return Card(child: ListTile(title: Text(title)));
  }
}
""",
    "components/chat_bubble.dart": """class ChatBubble extends StatelessWidget {
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
""",
    "components/visual_board_tile.dart": """class VisualBoardTile extends StatelessWidget {
  final String label;
  VisualBoardTile({required this.label});

  @override
  Widget build(BuildContext context) {
    return Card(child: Center(child: Text(label)));
  }
}
""",
    "services/auth_service.dart": """class AuthService {
  Future<bool> login(String email, String password) async {
    return email == "test@example.com" && password == "123456";
  }
}
""",
    "services/api_service.dart": """class ApiService {
  Future<String> fetchData(String endpoint) async {
    return "Mocked data from \$endpoint";
  }
}
""",
    "services/firebase_service.dart": """class FirebaseService {
  void initFirebase() {
    print("Firebase Initialized");
  }
}
""",
    "services/task_provider.dart": """class TaskProvider with ChangeNotifier {
  List<String> _tasks = [];
  List<String> get tasks => _tasks;

  void addTask(String task) {
    _tasks.add(task);
    notifyListeners();
  }
}
""",
    "services/assistant_provider.dart": """class AssistantProvider with ChangeNotifier {
  String _suggestion = "Take a break!";
  String get suggestion => _suggestion;

  void updateSuggestion(String newOne) {
    _suggestion = newOne;
    notifyListeners();
  }
}
""",
    "services/translation_service.dart": """class TranslationService {
  String translate(String input, String lang) {
    return "\$input (translated to \$lang)";
  }
}
""",
    "utils/constants.dart": 'const String APP_NAME = "Assistive App";',
    "utils/helpers.dart": 'String formatTime(DateTime dt) => "${dt.hour}:${dt.minute.toString().padLeft(2, \'0\')}";',
    "utils/theme.dart": """class AppTheme {
  static final lightTheme = ThemeData(
    primarySwatch: Colors.teal,
    visualDensity: VisualDensity.adaptivePlatformDensity,
  );
}
""",
    "utils/localization.dart": """class Localization {
  static String getText(String key) {
    return {
      "greet": "Hello",
      "bye": "Goodbye",
    }[key] ?? key;
  }
}
""",
    "utils/permissions_util.dart": """class PermissionsUtil {
  static Future<bool> requestMic() async {
    return true;
  }
}
""",
}

def create_flutter_files():
    for rel_path, content in files_structure.items():
        full_path = os.path.join(BASE_DIR, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"Created {full_path}")

if __name__ == "__main__":
    create_flutter_files()
