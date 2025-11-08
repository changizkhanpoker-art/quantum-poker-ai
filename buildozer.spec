[app]
title = MyPoker Quantum AI
package.name = mypokerquantum
package.domain = com.quantumpoker.ai

source.dir = src
source.include_exts = py,png,jpg,kv,txt,json,ttf

version = 1.0.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk_version = 25b
permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

p4a.branch = develop
android.allow_backup = true
android.accept_sdk_license = true

[ios]

[log]
