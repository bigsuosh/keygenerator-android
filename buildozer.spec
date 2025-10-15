[app]
title = KeyGeneratorApp
package.name = keygenerator
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 1.0
requirements = python3,kivy,plyer
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
orientation = portrait
android.arch = armeabi-v7a,arm64-v8a
# (Adjust sdk/ndk versions if needed)
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
