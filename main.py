from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread
import os, base64
try:
    from plyer import storagepath
except Exception:
    storagepath = None

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(16)
    spacing: dp(12)

    TextInput:
        id: filename
        hint_text: "Enter key file name (without extension)"
        multiline: False
        size_hint_y: None
        height: dp(48)

    Button:
        text: "Generate Key"
        size_hint_y: None
        height: dp(48)
        on_release: app.generate_key(filename.text)

    Label:
        id: status
        text: "Ready"
        size_hint_y: None
        height: dp(48)
'''

class Root(BoxLayout):
    pass

class KeyApp(App):
    def build(self):
        return Builder.load_string(KV)

    def get_downloads_dir(self):
        # Prefer plyer.storagepath if available (works on many devices).
        # Otherwise, fallback to common Android path.
        if storagepath:
            try:
                d = storagepath.get_downloads_dir()
                if d:
                    return d
            except Exception:
                pass
        # Common fallback
        possible = ['/sdcard/Download', '/storage/emulated/0/Download', os.path.expanduser('~/Downloads')]
        for p in possible:
            try:
                if os.path.isdir(p):
                    return p
            except Exception:
                continue
        # Last fallback: app-local directory
        return os.getcwd()

    @mainthread
    def set_status(self, text):
        try:
            self.root.ids.status.text = text
        except Exception:
            pass

    def generate_key(self, name):
        if not name or not name.strip():
            self.set_status("Please enter a file name.")
            return
        name = name.strip()
        file_name = name + ".key"
        downloads = self.get_downloads_dir()
        path = os.path.join(downloads, file_name)
        try:
            # Generate a Fernet-compatible key (32 random bytes base64 urlsafe)
            key = base64.urlsafe_b64encode(os.urandom(32))
            with open(path, "wb") as f:
                f.write(key)
            self.set_status(f"✅ Key saved to: {path}")
        except PermissionError:
            self.set_status("Permission denied. Grant storage permission in app settings.")
        except Exception as e:
            self.set_status("Error: " + str(e))

if __name__ == '__main__':
    KeyApp().run()
