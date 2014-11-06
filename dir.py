__author__ = 'Zeus'

import os
import file

class Dir:
    def __init__(self, path, parent, manifest):
        self.path = path
        self.parent = parent
        self.manifest = manifest

    def parse(self):
        for x in os.listdir(self.path):
            if os.path.isdir(self.path+"\\"+x):
                print("# Dir : "+self.path+" : Parse : Dir : "+x)
                tmp_dir = Dir(self.path+"\\"+x, self, self.manifest)
                self.manifest.add_dir(tmp_dir)
                tmp_dir.parse()
            else:
                print("# Dir : "+self.path+" : Parse : File : "+x)
                self.manifest.add_file(file.File(self.path+"\\"+x,self,self.manifest))