__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil


def clean_cache():
    my_path = r'/Users/viktoriya/WincAcademy/BACK/files/cache'
    if os.path.exists(my_path):
        shutil.rmtree(my_path)
    os.makedirs(my_path)


def cache_zip(filename, extract_dir):
    shutil.unpack_archive(filename, extract_dir)


def cached_files():
    my_path = os.path.abspath("files/cache")
    dir_cached_files = os.listdir(my_path)
    list_cached_files = []
    for file in dir_cached_files:
        list_cached_files.append(os.path.join(my_path, file))
    return list_cached_files


def find_password(list):
    for file in list:
        with open(file) as f:
            lines = f.readlines()
            for row in lines:
                if "password" in row:
                    return row.rsplit()[-1]
        f.close()
