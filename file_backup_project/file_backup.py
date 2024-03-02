import os
import shutil
from datetime import date

import datetime
import schedule
import time

source_dir = "C:/Users/TEXNO/OneDrive/Desktop/youtube_video_downloader"
destination_dir = "D:/Backup"

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination,str(today))


    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in {destination}")


schedule.every().day.at("10:30").do(lambda: copy_folder_to_directory(source_dir,destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)