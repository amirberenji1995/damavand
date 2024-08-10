import requests
import os
import time
import json
from zipfile import ZipFile
from rarfile import RarFile

def read_addresses():
   with open('datasets/addresses.json', 'r') as f:
      data = json.load(f)
   return data

class ZipDatasetDownloader():
    def __init__(self, url):
      self.url = url
      
    def download(self, download_file):
      self.download_file = download_file
      r = requests.get(self.url)
      with open(self.download_file, mode='wb') as file:
        file.write(r.content)
    
    def extract(self, extraction_path):
      self.extraction_path = extraction_path
      with ZipFile(self.download_file, 'r') as zObject:
        zObject.extractall(self.extraction_path)

    def download_extract(self, download_file, extraction_path):
    
      self.download(download_file)
      self.extract(extraction_path)

   
class CwruDownloader:
  def __init__(self, files):
    self.files = files
    self.undownloaded = {}

  def download(self, download_path, chunk_size = 512, delay = 1):
    self.download_path = download_path
    if not os.path.exists(self.download_path):
      os.makedirs(self.download_path)

    for key in self.files:
      print(f"Downloading: {key}")
      try:
        response = requests.get(self.files[key], stream=True)
        if response.status_code == 200:
          temp_file_path = os.path.join(self.download_path, key.split('.')[0] + ".tmp")

          with open(temp_file_path, mode="wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
              if chunk:
                file.write(chunk)

          os.rename(temp_file_path, os.path.join(self.download_path, key))
          print(f"Downloaded: {key}")
        else:
          print(f"Error downloading {key}: Response status {response.status_code}")
          self.undownloaded[key] = self.files[key]
          os.remove(temp_file_path)

      except Exception as e:
        print(f"Error downloading {key}: {e}")
        self.undownloaded[key] = self.files[key]
        os.remove(temp_file_path)

      time.sleep(delay)

  def redownload(self, chunk_size = 512, delay = 1):
    for key in list(self.undownloaded.keys()):
      print(f"Downloading: {key}")
      try:
        response = requests.get(self.files[key], stream=True)
        if response.status_code == 200:
          temp_file_path = os.path.join(self.download_path, key.split('.')[0] + ".tmp")

          with open(temp_file_path, mode="wb") as file:
              for chunk in response.iter_content(chunk_size=chunk_size):
                  if chunk:
                      file.write(chunk)

          os.rename(temp_file_path, os.path.join(self.download_path, key))
          self.undownloaded.pop(key)
          print(f"Downloaded: {key}")

        else:
          print(f"Error downloading {key}: Response status {response.status_code}")
          os.remove(temp_file_path)

      except Exception as e:
          print(f"Error downloading {key}: {e}")
          os.remove(temp_file_path)

      time.sleep(delay)

class PuDownloader():
  def __init__(self, files):
    self.files = files


  def download(self, download_path, timeout = 10):
    self.download_path = download_path
    if not os.path.exists(self.download_path):
      os.mkdir(self.download_path)
    for key in self.files.keys():
      for subkey in self.files[key]:
        print('Downloading: ', subkey)
        r = requests.get(self.files[key][subkey], stream = True, timeout=timeout)
        with open(self.download_path + subkey, 'wb') as f:
          f.write(r.content)

  def extract(self, extraction_path):
    self.extraction_path = extraction_path
    for key in self.files.keys():
      for subkey in self.files[key]:
        print('Extracting: ', subkey)
        with RarFile(self.download_path + subkey) as file:
          file.extractall(self.extraction_path)

  def download_extract(self, download_path, extraction_path, timeout = 10):
    
    self.download(download_path, timeout)
    self.extract(extraction_path)

class MaFaulDaDownloader():
  def __init__(self, files):
    self.files = files

  def download(self, download_path):
    self.download_path = download_path
    if not os.path.exists(self.download_path):
      os.mkdir(self.download_path)
    for key in self.files:
      print('Downloading: ', key)
      r = requests.get(self.files[key], stream = True)
      with open(self.download_path + key, 'wb') as f:
        f.write(r.content)

  def extract(self, extraction_path):
    self.extraction_path = extraction_path
    if not os.path.exists(self.download_path):
      os.mkdir(self.download_path)

    zip_files = [file for file in os.listdir(self.download_path) if file.endswith('.zip')]
    for zip_file in zip_files:
      print('Extracting: ', zip_file)
      with ZipFile(self.download_path + zip_file, 'r') as zObject:
        zObject.extractall(self.extraction_path)

  def download_extract(self, download_path, extraction_path):

    self.download(download_path)
    self.extract(extraction_path)