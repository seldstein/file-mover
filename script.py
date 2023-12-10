import shutil
import os

def move_goodreads_export(download_path, destination_path):
    try:
        # Check if the file exists
        if not os.path.isfile(download_path):
            print(f"No file found at {download_path}")
            return

        # Move the file
        shutil.move(download_path, destination_path)
        print(f"File moved to {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Update these paths
download_path = '~/Downloads/goodreads*.csv'  # e.g., '/Users/yourusername/Downloads/goodreads_export.csv'
destination_path = '~/Documents/my_other_brain/archives/exports/goodreads*.csv'  # e.g., '/Users/yourusername/Documents/goodreads_export.csv'

move_goodreads_export(download_path, destination_path)
