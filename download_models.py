import os
import gdown

# Google Drive folder ID (trích từ link của bạn)
folder_id = '1I-IoDYAKNFUBqgfS4482rBEoxgKyPZ4X'
output_dir = 'models'

os.makedirs(output_dir, exist_ok=True)

# Use gdown to download everything in the folder (requires shared folder to be public)
gdown.download_folder(id=folder_id, output=output_dir, quiet=False, use_cookies=False)
