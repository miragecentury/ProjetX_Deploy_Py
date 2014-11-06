__author__ = 'Zeus'

import os


class Manifest:
    def __init__(self, pathToDir):
        self.pathToDir = pathToDir
        self.Dirs = []
        self.Files = []
        self.localDirs = []
        self.localFiles = []
        self.localDir = []

    def parse(self):
        for x in os.listdir(self.pathToDir):
            if os.path.isdir(x):
                print()
            else:
                print()
    def addDir(self, dir):
        self.Dirs[dir.path] = dir
        print()

    def addFile(self, file):
        print()

    def create(self):
        print()