__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil


cache_path = os.path.join(os.getcwd(), 'files', 'cache')
zip_file = os.path.abspath('files/data.zip')


def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    else:
        pass
    os.makedirs(cache_path)


def cache_zip(filename, extract_dir):
    shutil.unpack_archive(filename, extract_dir)


def cached_files():
    dir_cached_files = os.listdir(cache_path)
    list_cached_files = []
    for file in dir_cached_files:
        list_cached_files.append(os.path.join(cache_path, file))
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
    clean_cache()
    cache_zip(zip_file, cache_path)
    files = cached_files()
    print(find_password(files))


if __name__ == "__main__":
    main()
