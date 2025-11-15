import kagglehub
import os
import shutil

def download_SP500_Data():
    #Returns the path of where the dataset was downloaded
    path = kagglehub.dataset_download("wmcginn/sp500-csv")
    print("Path to dataset files:", path)
    return path

folder_path = download_SP500_Data()
price_file = folder_path+"/prices.csv"
destination_file = "/Users/ayaanmunshi/Desktop/Coding/Projects/Market_Engine/data/processed/sp500_prices.csv"


shutil.copyfile(price_file, destination_file)
