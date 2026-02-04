[app]

# (str) Title of your application
title = BanglaDB

# (str) Package name
package.name = bangladb

# (str) Package domain (needed for android/ios packaging)
package.domain = org.bangladb

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# flask==2.2.5 এবং werkzeug==2.2.3 ব্যবহার করা হচ্ছে
requirements = python3,kivy==2.3.0,kivymd==1.1.1,flask==2.2.5,werkzeug==2.2.3,jinja2,itsdangerous,click,markupsafe,pillow,android,openssl

# (str) Icon of the application
icon.filename = logo.png

# (str) Presplash of the application
presplash.filename = logo.png

# (str) Presplash background color (for android)
# সাদা ব্যাকগ্রাউন্ড দেওয়া হলো যাতে গ্লিচ না হয়
android.presplash_color = #FFFFFF

# (str) Supported orientation (landscape, portrait, portrait-reverse or landscape-reverse)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# 🔥 FIX: API 33 থেকে কমিয়ে 31 (Android 12) করা হলো স্টেবল থাকার জন্য
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (bool) If True, then the application will be kept active when it is started
android.wakelock = True

# 🔥 CRITICAL FIX: Automatically accept SDK license
android.accept_sdk_license = True

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

# 🔥 CRITICAL FIX: AndroidX চালু করা হলো (Black Screen Crash Fix)
android.enable_androidx = True

# (list) Gradle dependencies to add
# মাঝে মাঝে AndroidX এর জন্য এই ডিপেন্ডেন্সি লাগে (অপশনাল, কিন্তু ভালো)
# android.gradle_dependencies = "androidx.appcompat:appcompat:1.4.2"

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
