__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil

zip_file = os.path.abspath('files/data.zip')


def cashe_path():
    if os.getcwd().endswith('files'):
        new_path = os.path.join(os.getcwd(), 'cache')
    else:
        new_path = os.path.join(os.getcwd(), 'files', 'cache')
    return new_path


def clean_cache():
    path = cashe_path()
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        pass
    os.makedirs(path)


def cache_zip(filename, extract_dir):
    shutil.unpack_archive(filename, extract_dir)


def cached_files():
    path = cashe_path()
    dir_cached_files = os.listdir(path)
    list_cached_files = []
    for file in dir_cached_files:
        list_cached_files.append(os.path.join(path, file))
    return list_cached_files


def find_password(list):
    for file in list:
        with open(file) as f:
            lines = f.readlines()
            for row in lines:
                if "password" in row:
                    return row.rsplit()[-1]
        f.close()


def main():
    path = cashe_path()
    clean_cache()
    cache_zip(zip_file, path)
    files = cached_files()
    print(find_password(files))


if __name__ == "__main__":
    main()
