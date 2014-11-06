__author__ = 'Zeus'

import os
import dir
import time


class Manifest:
    def __init__(self, pathToDir):
        self.pathToDir = pathToDir
        self.Dirs = list()
        self.Files = list()
        self.jsonData = {"Timestamp": time.time(), "Dirs": list(), "Files": list(), "FilesCRC": list()}

    def parse(self):
        dir_mods = dir.Dir(self.pathToDir+"\mods", self, self)
        dir_mods.parse()

    def add_dir(self, new_dir):
        self.Dirs.append(new_dir)

    def add_file(self, new_file):
        self.Files.append(new_file)

    def create(self):
        print("# Manifest:: Create")
        if os.path.exists(self.pathToDir+"\mods"):
            if os.path.isdir(self.pathToDir+"\mods"):
                print("# Manifest:: Directory \mods already exist")
            else:
                os.remove(self.pathToDir+"\mods")
                os.mkdir(self.pathToDir+"\mods")
                print("# Manifest:: Directory \mods create after delete the file")
        else:
            os.mkdir(self.pathToDir+"\mods")
            print("# Manifest:: Directory \mods create")
        self.parse()
        print("##############################")
        print("Nb Dirs = "+str(len(self.Dirs)))
        print("Nb Files = "+str(len(self.Files)))
        print("##############################")
        for xdir in self.Dirs:
            self.jsonData["Dirs"].append(xdir.path.replace(self.pathToDir+"\mods\\", ''))
        for xfile in self.Files:
            self.jsonData["Files"].append(xfile.path.replace(self.pathToDir+"\mods\\", ''))
            self.jsonData["FilesCRC"].append(xfile.CRC())
        print(self.jsonData)