import os
import os.path
import posixpath
import time


def backup_date(disk):
    
    unit = disk
    folder = ":\My_Backups"
    path = unit + folder
    path.replace(os.sep, posixpath.sep)
    files = os.listdir(path)
    #print(files)
    
    print("In the My_Backups folder you have the following files:")

    for file in files:
        current_path = disk + folder + "\\" + file
        #print(current_path)
        path.replace(os.sep, posixpath.sep)
        ti_m = os.path.getmtime(current_path)
        m_ti = time.ctime(ti_m)
        t_obj = time.strptime(m_ti)
        t_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
        print(f"{file} was created at {t_stamp}")
