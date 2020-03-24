#!/usr/bin/env python

import errno
import os
import subprocess
import sys

try:
    from DemonOverlord.core.demonoverlord import DemonOverlord

    modules_missing = False
except (ImportError, ModuleNotFoundError) as err:
    print(f"Missing module: {err}")
    modules_missing = True

modules_installed = False


def install_requirements():
    global modules_installed
    if not modules_installed:
        workdir = os.path.dirname(os.path.abspath(__file__))
        pip_cmd = ["pip3.8", 'install', '-Ur', os.path.join(workdir, "requirements.txt")]
        print('Missing required modules, trying to install them...')
        subprocess.run(pip_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        try:
            
            modules_installed = True
        except (OSError, subprocess.SubprocessError):
            print('Requirement update failed!')
            exit(errno.EINVAL)
    else:
        print('Trying to install missing requirements did not work, please contact the developers.')
        exit(errno.EINVAL)

def run():
    global modules_missing
    try:
        bot = DemonOverlord(sys.argv)
        bot.run(bot.config.token)
    except (ImportError, ModuleNotFoundError):
        modules_missing = True
        install_requirements()
        run()

if __name__ == "__main__":
    run()