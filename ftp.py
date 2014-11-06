__author__ = 'Hades'
import ftplib
import os


class ftp:

    def __init__(self, host, user, pawd):
        self.ftpco = ftplib(host)
        self.ftpco.login(user, pawd)

    def upload(self, path):
        ext = os.path.splitext(path)[1]
        if ext in (".txt", ".htm", ".html"):
            self.ftpco.storlines("STOR " + path, open(path))
        else:
            self.ftpco.storbinary("STOR " + path, open(path, "rb"), 1024)

    def remove(self,path):
        print("# FTP : REMOVE : "+path)
        self.ftpco.delete(path)

    def mkdir(self, path):
        print("# FTP : MKDIR : "+path)
        self.ftpco.mkd(path)

    def rmdir(self, path):
        print("# FTP : RMDIR : "+path)
        self.rmd(path)

    def close(self):
        self.ftpco.quit()