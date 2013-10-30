import pysftp

class Sftp(object):
    """ class for connect with sftp"""
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
	try:
            self.connection = pysftp.Connection(host = self.host, port = self.port, username = self.user,password = self.password)
            return True
        except:
            return False 

    def list_dir(self, path='.'):
        return self.connection.listdir(path = path)
    def current_working_dir(self):
        return self.connection.getcwd()
    def download_file(self,filename):
        self.connection.get(filemname)
