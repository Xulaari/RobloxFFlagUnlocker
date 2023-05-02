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

robloxsettings = {
    "DFIntTaskSchedulerTargetFps": fps
}

bloxstrapsettings = {
    "DFIntTaskSchedulerTargetFps": fps,
    "FFlagDebugGraphicsPreferD3D11": "True"
}

username = os.getlogin()

try:
    robloxversion = requests.get("https://setup.rbxcdn.com/version")
except Exception as k:
    print("There was an error requesting roblox's version, See: " + k)


robloxpath = f"C:\\Users\\{username}\\Appdata\\Local\\Roblox\\Versions\\{robloxversion.text}\\ClientSettings"
bloxstrappath = f"C:\\Users\\{username}\\AppData\\Local\\Bloxstrap\\Modifications\\ClientSettings"

print("Got roblox version at " + robloxversion.text[8:] + ". Adding FFlag.")

if os.path.exists(robloxpath) and not os.path.exists(bloxstrappath):
    try:
        print("ClientSettings Folder already found, Rewriting.")
    except Exception as q:
        print("An error occurred. See " + q)
if os.path.exists(robloxpath) and os.path.exists(bloxstrappath):
    try:
        print("Roblox and Bloxstrap Clientsettings folder found, Rewriting.")
    except Exception as q:
        print("An error occurred. See " + q)

def killroblox():
    for proc in psutil.process_iter():
        if proc.name() == "RobloxPlayerBeta.exe":
            proc.kill()
            break

def robloxwritefile():
    try:
      killroblox()
      os.makedirs(robloxpath, exist_ok=True)
      file_path = os.path.join(robloxpath, "ClientAppSettings.json")
      with open(file_path, "w") as f:
         json.dump(robloxsettings, f, indent=4)
    except Exception as v:
      print("An error occured. See:  " + v)

def bloxstrapwritefile():
    try:
      killroblox()
      os.makedirs(bloxstrappath, exist_ok=True)
      file_path = os.path.join(bloxstrappath, "ClientAppSettings.json")
      with open(file_path, "w") as f:
         json.dump(bloxstrapsettings, f, indent=4)
    except Exception as n:
        print("An error occured. See: " + n)

if refreshrate >= 60 and os.path.exists(robloxpath):
    robloxwritefile()
elif refreshrate >= 60 and os.path.exists(bloxstrappath):
    bloxstrapwritefile()
if refreshrate >= 60 and os.path.exists(robloxpath) and os.path.exists(bloxstrappath):
    robloxwritefile()
    bloxstrapwritefile()
if refreshrate >= 60 and not os.path.exists(robloxpath):
    os.mkdir(os.path.join(f"C:\\Users\\{username}\\Appdata\\Local\\Roblox\\Versions\\{robloxversion.text}"))
    robloxwritefile()
if refreshrate >= 60 and not os.path.exists(bloxstrappath):
    os.mkdir(os.path.join(f"C:\\Users\\{username}\\AppData\\Local\\Bloxstrap\\Modifications\\ClientSettings"))
    bloxstrapwritefile()

input("FFlag added. \x1b[39mPress \x1b[32m[Enter]\x1b[39m to exit. ")
