import os
import sys
from time import sleep
import platform

is_python_installed = os.system("python3 --version") == 0

if is_python_installed:
    print("Python is installed, proceeding with runtime.")
else:
    if sys.platform == "win32":
        print("Python is not installed, taking you to the Microsoft Store.")
        os.system("start ms-windows-store://pdp/?ProductId=9NCVDN91XZQP")
    elif sys.platform == "linux":
        print("Python is not installed, taking you to the Python website.")
        os.system("xdg-open https://www.python.org/downloads/")
    elif sys.platform == "darwin":
        print("Python is not installed, taking you to the Python website.")
        os.system("open https://www.python.org/downloads/")
    else:
        print("Python is not installed, please install it manually.")
        sys.exit(1)

attempts = 0
while not is_python_installed and attempts < 12:
    print("Waiting for Python to be installed...")
    is_python_installed = os.system("python3 --version") == 0
    sleep(5)
    attempts += 1

if not is_python_installed:
    print("Python installation check exceeded maximum attempts. Exiting.")
    sys.exit(1)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
version = os.system(
    f'python3 {os.path.abspath("./updater.py")}\
 --name "OP Media Player"\
 --version {open(os.path.abspath("./ver")).read().strip()}\
 --file-index-path {os.path.abspath("./remove_index.json")}\
 --root-path "{os.path.abspath(".")}/"'
)
os.system("python3 Main.py")
