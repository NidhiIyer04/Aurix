class Localization {
  static String getText(String key) {
    return {
      "greet": "Hello",
      "bye": "Goodbye",
    }[key] ?? key;
  }
}
