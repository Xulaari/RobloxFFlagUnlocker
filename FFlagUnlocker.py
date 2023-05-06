print("\x1b[36mLoading Imports, Wait.\x1b[39m")

import requests
import os
import win32api

os.system("cls")

refreshrate = win32api.EnumDisplaySettings(None, 0).DisplayFrequency

print(
    "\x1b[36mFFlagUnlocker\x1b[39m | Coded in python and built with love by \x1b[31mxula!\x1b[39m\n"
)

robloxversion = requests.get("https://setup.rbxcdn.com/version").text
robloxversionreadable = requests.get("https://setup.rbxcdn.com/version").text.replace(
    "version-", ""
)

print(f"Roblox version gateway at: {robloxversionreadable}")
takeinnoyes = input(
    f"{os.getlogin()}, Press any key \x1b[36m[Enter]\x1b[39m to make FPS Cap your monitors HZ or \x1b[36m:q\x1b[39m To set a custom one: "
)

if not os.path.exists(
    f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings"
):
    os.mkdir(
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings"
    )

try:
    if takeinnoyes == ":q":
        os.system("cls")
        print("\x1b[39mFFlagUnlocker. Built with love by \x1b[31mxula!\x1b[39m\n")
        fpscapifcustom = int(
            input("Detected \x1b[36m:q\x1b[39m. Enter what FPS Cap to set: \x1b[36m")
        )
        print("\x1b[39mApplying \x1b[36m:q\x1b[39m settings.")
        with open(
            f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings\\ClientAppSettings.json",
            "w",
        ) as nvm:
            nvm.write(
                f"""{{
    "DFIntTaskSchedulerTargetFps": {fpscapifcustom}
}}"""
            )
    else:
        print("Applying default settings.")
        with open(
            f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions\\{robloxversion}\\ClientSettings\\ClientAppSettings.json",
            "w",
        ) as nvm:
            nvm.write(
                f"""{{
    "DFIntTaskSchedulerTargetFps": {refreshrate}
}}"""
            )
except FileNotFoundError or NotADirectoryError:
    print("Your roblox is out of date from the newest version.")

input(
    "Press any key to exit. Thank you for using the \x1b[36mM1\x1b[39m version of \x1b[36mFFlagUnlocker!\x1b[39m"
)
exit()
