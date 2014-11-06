__author__ = 'Hades'
import ftplib
import os


class ftp:

    def __init__(self, host, user, pawd):
        self.ftpco = ftplib.FTP(host)
        self.ftpco.login(user, pawd)

    def read(self, path, callback):
        return self.ftpco.retrbinary('RETR '+path, callback)

    def dir(self, path):
        return self.ftpco.dir(path)

    def upload(self, ftppath, path):
        print("# FTP : UPLOAD : "+path+" TO "+ftppath)
        ext = os.path.splitext(path)[1]
        self.ftpco.storbinary("STOR " + ftppath, open(path, "rb"), 1024)

    def remove(self, path):
        print("# FTP : REMOVE : "+path)
        self.ftpco.delete(path)

    def mkdir(self, path):
        print("# FTP : MKDIR : "+path)
        self.ftpco.mkd(path)

    def rmdir(self, path):
        print("# FTP : RMDIR : "+path)
        self.ftpco.rmd(path)

    def close(self):
        self.ftpco.quit()