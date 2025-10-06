import os

os.getcwd()
os.mkdir("test_dir_from_python")
os.mkdir("test_dir_from_python/subdir1")
os.makedirs("test_dir_from_python/subdir2/subdir2.1")
os.makedirs("test_dir_from_python/subdir2/", exist_ok=True)
os.listdir("test_dir_from_python")

my_file_path = 'test_dir_from_python/subdir1/script.py'

os.path.basename(my_file_path)


#This command will write hello to terminal
print("hello!")

