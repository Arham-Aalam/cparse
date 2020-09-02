import os
import re

from .constants import Constant

def _find_all_file_paths(root_path):
    if root_path is None:
        raise Exception("Please provide project root path.")

    if not os.path.exists(root_path):
        raise Exception(f"Path {root_path} not exists")

    q = []
    q.append(root_path)

    files = []
    while len(q) != 0:
        curr = q.pop(0)
        fs = os.listdir(curr)
        # all folders to queue
        for f in fs:
            if os.path.isdir(os.path.join(curr, f)):
                q.append(os.path.join(curr, f))
        # filter files only
        fs = [os.path.join(curr, f) for f in fs if os.path.isfile(os.path.join(curr, f))]
        files += fs
    
    return files

def _parse_urls(files):
    urls_dict = {}
    for file in files:
        file_content = open(file, 'r').read()
        match = re.findall(Constant.URL_REGEX, file_content)
        urls_dict[file] = match

    return urls_dict