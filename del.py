import os
import glob
from datetime import datetime, timedelta

def delete_old_files(folder_path, file_extensions):
    # Get the current date and time
    current_datetime = datetime.now()

    # Calculate the threshold date (2 days ago)
    threshold_datetime = current_datetime - timedelta(days=2)

    # Construct a glob pattern to match files with specified extensions
    file_pattern = os.path.join(folder_path, f"*.{file_extensions}")

    # Iterate through matched files
    for file_path in glob.glob(file_pattern):
        # Get file creation time
        creation_time = os.path.getctime(file_path)
        creation_datetime = datetime.fromtimestamp(creation_time)

        # Check if the file is older than 2 days
        if creation_datetime < threshold_datetime:
            try:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

# Use a raw string for the folder path
folder_path = r'F:\Bodycam\Grand Theft Auto V'
# Include 'jpg', 'png', 'mp4', and 'dvr' in the file extensions
file_extensions = 'jpg|png|mp4|dvr'

delete_old_files(folder_path, file_extensions)
