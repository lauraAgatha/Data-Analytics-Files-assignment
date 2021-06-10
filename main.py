__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile

folder = os.getcwd() # volgens de wincpy check klopt het nu, als ik normaal de code run in VS, moet hier het volgende achteraan geplakt:  + "\\" + "files"
cache_dir = folder + "\cache"
zip_path = folder + "\data.zip"

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

cache_zip(zip_path, cache_dir)

# Excercise 3
def cached_files():
    cached_files = []
    for file in os.listdir(cache_dir):
        cached_files.append(os.path.join(cache_dir, file))
    return cached_files

cached_files()

# Excercise 4
def find_password(cached_files):
    search_pw = "password"
    for file in cached_files:
        f = open(file, "r")
        # for line in f:
        for line in f.readlines():
            password = None
            if search_pw in line:
                password = line.split(": ")[1][:-1]
                print(password)
                return password

find_password(cached_files())