# Siri Shortcut to Start Jarvis

This folder demonstrates how you can start a simple Jarvis script using Siri.

The included files are:

- `jarvis.py` – a minimal Python script that represents the Jarvis assistant.
- `start_jarvis.applescript` – AppleScript used by the Siri Shortcut to run `jarvis.py`.

## Creating the Shortcut

1. Open the **Shortcuts** app on macOS.
2. Create a new shortcut and name it **Jarvis**.
3. Add the **Run AppleScript** action.
4. Paste the contents of `start_jarvis.applescript` into the action.
   Make sure to update the path to `jarvis.py` in the script.
5. Save the shortcut.
6. In the shortcut settings, assign the voice phrase `"Hey Siri, open Jarvis"`.

Now, whenever you say *"Hey Siri, open Jarvis"*, macOS will execute the
AppleScript, which in turn launches the Python script.
