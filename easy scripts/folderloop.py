import os

#enter the path where the dir should be created
path = "c:/Users/Ramyashree Shetty/Desktop"
new_dir = "loop"
new_dir_path = os.path.join(path,new_dir)
os.mkdir(new_dir_path)

#enter the no of files you desire
no_of_files=5

while(no_of_files != 0):
    dir = new_dir + str(no_of_files)
    new_path = os.path.join(new_dir_path,dir)
    os.mkdir(new_path)
    no_of_files=no_of_files-1
