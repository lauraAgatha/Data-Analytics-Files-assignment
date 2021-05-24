__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile

cache_dir = r'D:\Documenten\Trainingen\Wincademy\files\cache'
zip_path = r'D:\Documenten\Trainingen\Wincademy\files\data.zip'

# Excercise 1
def clean_cache():

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        print("Created Directory : ", cache_dir)
    else:
        shutil.rmtree(cache_dir)
        print("Directory already existed : ", dir)


clean_cache()

# Excercise 2
def cache_zip(zip_path, cache_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir)


print(cache_zip(zip_path, cache_dir))

# Excercise 3
def cached_files():
    abs_cache_dir = os.path.abspath(cache_dir)
    cached_files = []
    for file in os.listdir(abs_cache_dir):
        cached_files.append(f"{abs_cache_dir}\{file}")
    print(cached_files)
    return cached_files


cached_files()

# Excercise 4
def find_password(cached_files):
    search_pw = "password"
    for file in cached_files:
        f = open(file, "r")
        if search_pw in f.read():
            #f.read().replace(" ", "")
            password = f.read().split(":")
            print(password)
            print(file)


find_password(cached_files())