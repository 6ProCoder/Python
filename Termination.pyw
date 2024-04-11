import sys
import os
import time

time.sleep(60*30) #60 is one minute and in the other you put as many minutes as you want

def main():

    if sys.platform == "win32":
        os.system("shutdown /s /t 1")
    else:
        os.system("shutdown -h now")

if __name__ == "__main__":
    main()
