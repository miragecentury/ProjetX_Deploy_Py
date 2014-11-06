__author__ = 'Zeus'

import sys
import os
import manifest


def check_dir_format():
    if os.path.exists(sys.argv[1]+"/mods"):
        if os.path.exists(sys.argv[1]+"/manifest.json"):
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
            print("# Repository Dir : "+sys.argv[1])
            if sys.argv[2] == "status":
                if check_dir_format():
                    print("# Command: Status")
                    mani = manifest.Manifest(sys.argv[1])
                    mani.status()
                else:
                    print("# Is Not A Repository")
            elif sys.argv[2] == "deploy":
                if check_dir_format():
                    if len(sys.argv) >6:
                        print("# Command: deploy")
                        mani = manifest.Manifest(sys.argv[1])
                        mani.deploy(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
                    else:
                        print("# Usage : deploy host user passwd")
                else:
                    print("# Is Not A Repository")
            elif sys.argv[2] == "create":
                if check_dir_format():
                    print("# Repository already create")
                else:
                    print("# Is Not A Repository, it will be create")
                    print("# Command: create")
                    mani = manifest.Manifest(sys.argv[1])
                    mani.create()

            else:
                print("# Usage : [status|deploy]")
        else:
            print("# Path is not exist or not a directory")
    else:
        print("# Arguments Insufficient ")