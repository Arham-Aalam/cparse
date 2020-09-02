import os
import argparse
from . import utils 

def _init_args():
    parser = argparse.ArgumentParser(description='Cparse Tool')
    parser.add_argument('--rootpath', help='Root path of the project.', default=None)
    parser.add_argument('--outpath', help='output path of the report.', default=None)

    return parser.parse_args()

def _run(_args=None):
    args = _init_args()
    
    if _args is not None:
        args = _args
    
    files = utils._find_all_file_paths(args.rootpath)
    urls_ = utils._parse_urls(files)
    print(urls_)
