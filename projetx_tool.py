__author__ = 'Zeus'

import sys
import os


def check_dir_format():
    if os.path.exists(sys.argv[1]+"/mods"):
        if(os.path.exists(sys.argv[1]+"/manifest.json")):
            return True
        else:
            return False
    else:
        return False

if "__main__" == __name__:
    print("########################################")
    print("# ProjetX_Command_Line = version 0.0.1 #")
    print("########################################")
    if len(sys.argv) > 2:
        #Check Path at argument
        if os.path.exists(sys.argv[1]) and os.path.isdir(sys.argv[1]):
            if sys.argv[2] == "status":
                print("Command: status")
            elif sys.argv[2] == "deploy":
                print("Command: deploy")
            elif sys.argv[2] == "create":
                print("Command: create")
            else:
                print("Usage : [status|deploy]")
        else:
            print("Path is not exist or not a directory")
    else:
        print("insuffisent arguments ")