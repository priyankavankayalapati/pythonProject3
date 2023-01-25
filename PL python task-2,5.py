import os
import logging
logging.basicConfig(level=logging.INFO)
directory = "C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files"
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith('.csv') or file_path.endswith('.txt'):
            logging.info('File path: %s', file_path)
        else:
            logging.error('Invalid file type: %s', file_path)

