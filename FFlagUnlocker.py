import requests
import os
import json
import numpy
import win32api
import psutil

print("Software by \x1b[34mxula\x1b[34m!")
addto = input("\x1b[39mPress \x1b[32m[Enter]\x1b[39m to use your monitors HZ or enter what to add on or takeaway : ")

refreshrate = win32api.EnumDisplaySettings(None, 0).DisplayFrequency

if addto == "":
    fps = int(numpy.ceil(refreshrate) + 1)
else:
    fps = int(numpy.ceil(refreshrate) + float(addto))

settings = {
    "DFIntTaskSchedulerTargetFps": fps
}

username = os.getlogin()

try:
    rbxv = requests.get("https://setup.rbxcdn.com/version")
except Exception as k:
    print("There was an error requesting roblox's version.")


rbxpth = f"C:\\Users\\{username}\\Appdata\\Local\\Roblox\\Versions\\{rbxv.text}\\ClientSettings"

print("Got roblox version at " + rbxv.text[8:] + ". Adding FFlag.")

if os.path.exists(rbxpth):
    try:
        print("ClientSettings Folder already found, Rewriting.")
    except Exception as q:
        print("An error occurred. See " + q)

def killroblox():
    for proc in psutil.process_iter():
        if proc.name() == "RobloxPlayerBeta.exe":
            proc.kill()
            break

def writefile():
    try:
      killroblox()
      os.makedirs(rbxpth, exist_ok=True)
      file_path = os.path.join(rbxpth, "ClientAppSettings.json")
      with open(file_path, "w") as f:
         json.dump(settings, f, indent=4)
    except Exception as k:
      print("An error has happened | " + k)

if refreshrate >= 60:
    writefile()
else:
    print("FFlag not added. Refresh Rate detected as {refreshrate}. ")

input("FFlag added. \x1b[39mPress \x1b[32m[Enter]\x1b[39m to exit. ")
