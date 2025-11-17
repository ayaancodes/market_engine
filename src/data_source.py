import kagglehub
import os
import shutil

def download_XAUGold_Data():
    #Returns the path of where the dataset was downloaded
    path = kagglehub.dataset_download("novandraanugrah/xauusd-gold-price-historical-data-2004-2024")
    print("Path to dataset files:", path)
    return path

folder_path = download_XAUGold_Data()
print("Files in the folder:", os.listdir(folder_path))
single_day_pricing = folder_path+"/XAU_1d_data.csv"
destination_file = "/Users/ayaanmunshi/Desktop/Coding/Projects/Market_Engine/data/processed/xau_daily.csv"


shutil.copyfile(single_day_pricing, destination_file)
