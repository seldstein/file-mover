import shutil
import os

def goodreads_export(download_path, destination_path):
    try:
        if not os.path.isfile(download_path):
            print(f"No file found at {download_path}")
            return

        shutil.move(download_path, destination_path)
        print(f"File moved to {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

download_path = '~/Downloads/goodreads*.csv'
destination_path = '~/Documents/my_other_brain/archives/exports/goodreads*.csv'

goodreads_export(download_path, destination_path)
