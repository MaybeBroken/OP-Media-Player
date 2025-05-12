import os
import sys
import shutil
from tkinter import messagebox

if sys.platform == "win32":
    userAppData = os.getenv("APPDATA")
elif sys.platform == "linux":
    userAppData = os.path.expanduser("~/.local/share")
elif sys.platform == "darwin":
    userAppData = os.path.expanduser("~/Library/Application Support")
appId = "OP-Media-Player"

if not os.path.exists(os.path.join(userAppData, appId)):
    os.makedirs(os.path.join(userAppData, appId))

os.chdir(os.path.abspath(os.path.dirname(__file__)))

if messagebox.askyesno(
    "OP Media Player Installer",
    "Would you like to install OP Media Player?",
):
    try:
        shutil.unpack_archive("Releases/0.0.7_mac.zip", os.path.join(userAppData, appId))
    except Exception as e:
        messagebox.showerror(
            "Installation Error",
            f"An error occurred during installation: {e}\n{os.listdir()}",
        )
        sys.exit(1)
    messagebox.showinfo(
        "Installation Complete",
        "OP Media Player has been successfully installed.",
    )
else:
    print("Installation cancelled.")
    sys.exit(0)
