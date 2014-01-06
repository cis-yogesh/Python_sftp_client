"""
This is sample example code for track file which have no data is moved to zero data files directory.
"""
hostname = 'example.com'
port = 22
username= 'sftp-user'
password= '12@abc'
localpath = '/home/user/Desktop/'
from sftp import *

ftp = Connection(host = hostname,port = port, username = username, password = password)
file_list = ftp.listdir(path='.')
for i in file_list:
    if '.' in i:
        size = ftp.get_file_size(i)
        if not size:
            ftp.rename(i, 'zero_data_files/'+i)
        else:
            ftp.get(i, localpath+i)
            ftp.put(localpath+i,'oldfiles/'+i)
ftp.close()
