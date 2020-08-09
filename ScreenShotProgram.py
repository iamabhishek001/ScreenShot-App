import pyautogui
import os
from plyer import notification

files = os.listdir()
if "ScreenShots" not in files:
    os.makedirs("ScreenShots")

pyautogui._snapshot("ScreenShot", "ScreenShots")
notification.notify(
    app_icon="App Comp\\Icons\\setup_icon.ico",
    title = "ScreenShot",
    message="ScreenShot Taken",
    timeout=2
)
