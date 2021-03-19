import os
import sys
import requests
from zipfile import ZipFile
from tqdm import tqdm

download_path = 'data/temp/'

def download(url, destination_file):
    directory, local_filename = os.path.split(destination_file)
    
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
            
    req = requests.get(url, stream=True)
    file_size = int(req.headers['Content-Length'])
    chunk_size = 1024  # 1 MB
    num_bars = int(file_size / chunk_size)

    with open(destination_file, 'wb') as fp:
        for chunk in tqdm(req.iter_content(chunk_size=chunk_size), total=num_bars, unit='KB', desc=local_filename, leave=True, file=sys.stdout):
            fp.write(chunk)

    return destination_file

def unzip(file, destination_path):
    if not os.path.exists(destination_path):
        try:
            os.makedirs(destination_path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
                
    # Open your .zip file
    with ZipFile(file=file) as zip_file:

        # Loop over each file
        for file in tqdm(iterable=zip_file.namelist(), total=len(zip_file.namelist())):

            # Extract each file to another directory
            # If you want to extract to current working directory, don't specify path
            zip_file.extract(member=file, path=destination_path)