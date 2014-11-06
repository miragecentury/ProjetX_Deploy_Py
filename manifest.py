__author__ = 'Zeus'

import os
import dir
import time
import json


class Manifest:
    def __init__(self, pathToDir):
        self.pathToDir = pathToDir
        self.Dirs = list()
        self.Files = list()
        self.ADirs = {}
        self.AFiles = {}

    def parse(self):
        dir_mods = dir.Dir(self.pathToDir+"\mods", self, self)
        dir_mods.parse()

    def add_dir(self, new_dir):
        self.Dirs.append(new_dir)
        self.ADirs[os.path.normcase(new_dir.path)] = new_dir

    def add_file(self, new_file):
        self.Files.append(new_file)
        self.AFiles[os.path.normcase(new_file.path)] = new_file

    def status(self):
        print("# Manifest:: Status")
        self.parse()
        fmani = open(self.pathToDir+"\manifest.json", "r")
        jsonDataMani = fmani.read()
        jsonData = json.loads(jsonDataMani)
        #Check Dir
        currentDirs = list()
        for xdir in self.Dirs:
            currentDirs.append(xdir.path.replace(self.pathToDir+"\mods"+os.sep, ''))
        similarDirs = list()
        eraseDirs = list()
        createDirs = list()
        for xdir in (set(currentDirs).intersection(set(jsonData["Dirs"]))):
            similarDirs.append(xdir)
        for xdir in (set(currentDirs).difference(set(currentDirs).intersection(set(jsonData["Dirs"])))):
            createDirs.append(xdir)
        for xdir in (set(jsonData["Dirs"]).difference(set(currentDirs).intersection(set(jsonData["Dirs"])))):
            eraseDirs.append(xdir)
        print("# Manifest : Status : Similar Dirs = "+str(similarDirs))
        print("# Manifest : Status : Erase Dirs = "+str(eraseDirs))
        print("# Manifest : Status : Create Dirs = "+str(createDirs))

        #Check File
        currentFiles = list()
        currentFilesCRC = list()
        for xfile in self.Files:
            currentFiles.append(xfile.path.replace(self.pathToDir+"\mods"+os.sep, ''))
            currentFilesCRC.append(xfile.CRC())
        similarFiles = list()
        eraseFiles = list()
        createFiles = list()
        modifiedFiles = list()
        for xdir in (set(currentFiles).intersection(set(jsonData["Files"]))):
            similarFiles.append(xdir)
        for xdir in (set(currentFiles).difference(set(currentFiles).intersection(set(jsonData["Files"])))):
            createFiles.append(xdir)
        for xdir in (set(jsonData["Files"]).difference(set(currentFiles).intersection(set(jsonData["Files"])))):
            eraseFiles.append(xdir)
        for xfile in similarFiles:
            currentCRC = self.AFiles[os.path.normcase(self.pathToDir+os.sep+"mods"+os.sep+xfile)].CRC()
            manifestCRC = jsonData["FilesCRC"][jsonData["Files"].index(xfile)]
            if(currentCRC != manifestCRC):
                print(xfile)
                modifiedFiles.append(xfile)
                similarFiles.remove(xfile)
        print("# Manifest : Status : Similar Files = "+str(similarFiles))
        print("# Manifest : Status : Erase Files = "+str(eraseFiles))
        print("# Manifest : Status : Create Files = "+str(createFiles))
        print("# Manifest : Status : Modify Files = "+str(modifiedFiles))
        return {
            "sd": similarDirs,
            "cd": createDirs,
            "ed": eraseDirs,
            "sf": similarFiles,
            "cf": createFiles,
            "ef": eraseFiles,
            "mf": modifiedFiles
        }

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
        jsonData = {"Timestamp": time.time(), "Dirs": list(), "Files": list(), "FilesCRC": list()}
        for xdir in self.Dirs:
            jsonData["Dirs"].append(xdir.path.replace(self.pathToDir+"\mods"+os.sep, ''))
        for xfile in self.Files:
            jsonData["Files"].append(xfile.path.replace(self.pathToDir+"\mods"+os.sep, ''))
            jsonData["FilesCRC"].append(xfile.CRC())
        jsonDataStr = json.dumps(jsonData)
        f = open(self.pathToDir+"\manifest.json", "w")
        f.write(jsonDataStr)
        f.close()