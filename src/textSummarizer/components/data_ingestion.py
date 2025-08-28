import os, urllib.request as request,zipfile
from src.textSummarizer.logging import logging
from src.textSummarizer.entity import DataIngestionConfig
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(url=self.config.source_URL,filename=self.config.local_data_file)
            logging.info(f"File is downloaded")
        else:
            logging.info(f"File alread exists")
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)