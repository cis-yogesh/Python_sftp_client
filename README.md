djangosftp
==========

sftp app for django to connect sftp server

Download and run ./setup.py install

create a sftp object:

from  django_sftp import Sftp
sftp_obj = Sftp(host, port, user, password)
result = sftp_obj.connect()
check connection 
if result :
    sftp_obj.list_dir(path='.') # path is your listing path of os
    sftp_obj.current_working_dir() # return current working dir of remote os
    sftp_obj.download_file(your_filename) # file name that you want to download.
