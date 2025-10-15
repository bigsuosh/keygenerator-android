KeyGeneratorApp (Kivy)
======================

What this project is
- A simple Android app (Kivy) that generates a Fernet-compatible key and saves it to the device's Downloads folder.
- UI: one TextInput for filename + one button to generate the key.

Important note
- This environment cannot build an APK for you (Android SDK/NDK and buildozer are required).
- Instead, this ZIP contains a ready-to-build project. You can build the APK locally (recommended on Linux) or using a CI runner (GitHub Actions).

Quick build steps (Linux, recommended)
1. Install system deps (Ubuntu example):
   sudo apt update && sudo apt install -y python3-pip python3-setuptools git zip unzip openjdk-11-jdk

2. Install buildozer and dependencies in a virtualenv (recommended):
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install buildozer

3. Initialize/build (already has buildozer.spec in project root):
   cd KeyGeneratorApp
   buildozer android debug

   The first run downloads Android SDK/NDK and other tools (takes time).
   The generated APK will be in bin/ (e.g., bin/keygenerator-1.0-debug.apk).

Alternative: Use GitHub Actions / cloud builder
- You can set up a GitHub Actions workflow that runs buildozer on an ubuntu-latest runner to produce the APK automatically.
- Let me know if you want a ready GitHub Actions YAML for that.

Runtime permissions on Android 11+
- The app requests external storage permissions. On modern Android versions, you may need to allow "Files and media" permission manually or adapt the app to use scoped storage (using SAF).

Customization
- If you want the key displayed on-screen (instead of saving), or copied to clipboard, I can modify the code.

