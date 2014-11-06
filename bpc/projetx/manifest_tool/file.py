__author__ = 'Zeus'

import zlib


class File:
    def __init__(self, path, parent, manifest):
        self.path = path
        self.parent = parent
        self.manifest = manifest

    def check(self):
        print()

    def CRC(self):
        prev = 0
        for eachLine in open(self.path, "rb"):
            prev = zlib.crc32(eachLine, prev)
        return "%X" % (prev & 0xFFFFFFFF)