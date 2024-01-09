import shutil
import os

def move_files(download_path, destination_path, filenames):
    try:
        for filename in filenames:
            source_file = os.path.join(download_path, filename)
            destination_file = os.path.join(destination_path, filename)

            if os.path.exists(source_file):
                shutil.move(source_file, destination_file)
                print(f"File '{filename}' moved to {destination_path}")
            else:
                print(f"File '{filename}' not found in {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

download_path = os.path.expanduser('~/Downloads/')
destination_path = os.path.expanduser('~/Documents/my_other_brain/archives/exports/')
files_moved = ["goodreads_library_export.csv", "calendar.ics"]

move_files(download_path, destination_path, files_moved)

0 0 1 * * usr/bin/python3 /Users/Samfeld/repos/to/file-mover/script.py