import requests
import os
import win32api
import time

refreshrate = win32api.EnumDisplaySettings(None, 0).DisplayFrequency

print("\x1b[36mFFlagUnlocker\x1b[39m | Coded in python and built with love by \x1b[31mxula!\x1b[39m\n")

robloxversion = requests.get("https://setup.rbxcdn.com/version").text
robloxversionreadable = requests.get("https://setup.rbxcdn.com/version").text.replace('version-', '')

print(f"Roblox version gateway at: {robloxversionreadable}")
takeinnoyes = input(f"{os.getlogin()}, Press any key \x1b[36m[Enter]\x1b[39m to make FPS Cap your monitors HZ or \x1b[36m:q\x1b[39m To set a custom one: ")

if not os.path.exists(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\ClientSettings"):
    os.mkdir(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\ClientSettings")

try:
    if takeinnoyes == ":q":
        os.system('cls')
        print("\x1b[39mFFlagUnlocker. Built with love by \x1b[31mxula!\x1b[39m\n")
        fpscapifcustom = int(input("Detected \x1b[36m:q\x1b[39m. Enter what FPS Cap to set: "))
        print("Applying custom settings.")
        with open(f"C:\\Users\\{os.getlogin()}\\Appdata\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings\\ClientAppSettings.json", 'w') as nv:
            nv.write(f"""{{
    "DFIntTaskSchedulerTargetFps": {fpscapifcustom}
}}""")
    elif refreshrate <= 60:
        print(f"HZ {refreshrate}. Not applied. Closing.")
        time.sleep(3)
        exit()
    else:
        print("Applying default settings.")
        with open(f"C:\\Users\\{os.getlogin()}\\Appdata\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings\\ClientAppSettings.json", 'w') as n:
            n.write(f"""{{
    "DFIntTaskSchedulerTargetFps": {refreshrate}
}}""")
except FileNotFoundError or NotADirectoryError:
    print("Your roblox is out of date from the newest version.")

input("Press any key to exit. Thank you for using the \x1b[36mM1\x1b[39m version of \x1b[36mFFlagUnlocker!\x1b[39m")
exit()