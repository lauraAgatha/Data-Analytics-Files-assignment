__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile

cache_dir = os.path.abspath("cache")
# cache_dir = r'D:\Documenten\Trainingen\Wincademy\files\cache'
zip_path = r'D:\Documenten\Trainingen\Wincademy\files\data.zip'

# Excercise 1
def clean_cache():
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print("Directory already existed : ", dir)
    else:
        os.makedirs(cache_dir)
        print("Created Directory : ", cache_dir)

clean_cache()

# Excercise 2
def cache_zip(zip_path, cache_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir)

print(cache_zip(zip_path, cache_dir))

# Excercise 3
def cached_files():
    cached_files = []
    for file in os.listdir(cache_dir):
        cached_files.append(f"{cache_dir}\{file}")
    return cached_files

cached_files()


# PLEASE READ THIS COMMENT:
# I adjusted this assignment with your feedback and you explained to change the forloop as in the comments, which was what I did.
# In both versions I got the password printed if you do print(password), but I still get thumbs down for the last find password.
# Excercise 4
def find_password(cached_files):
    search_pw = "password"
    for file in cached_files:
        f = open(file, "r")
        # for line in f:
        for line in f.readlines():
            password = None
            if search_pw in line:
                password = line.split(": ")[1]
                return password

find_password(cached_files())