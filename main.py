# This script will help you to download the Etsy images from your shop's export csv into SKU folders
# Script author: Mazen Alsenih (mazensenih.com | mazen.el.senih@gmail.com)
# Hope it helps you. 😉
# Usage: python main.py <path_to_file>

# Libraries
import os
import sys
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

def download_image(image_url, dest_folder, image_number):
    if pd.notna(image_url):
        try:
            # Send a GET request to the image URL
            response = requests.get(image_url, stream=True)
            # Check if the request was successful
            if response.status_code == 200:
                image_filename = f"IMAGE{image_number}.jpg"
                image_path = os.path.join(dest_folder, image_filename)
                # Open the image file to write the content
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {image_url} to {image_path}")
            else:
                print(f"Failed to download {image_url}. HTTP status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to download {image_url}. Error: {e}")

def main(file_path):
    # Extract the filename without extension and construct the base directory
    base_filename = Path(file_path).stem
    base_dir = Path(f"{base_filename}_etsy_images")

    # Check the file extension and read the file accordingly
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        print("Unsupported file format. Please provide a .csv or .xlsx file.")
        return

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        # Get the SKU and prepare the directory name
        sku = str(row['SKU'])
        sku_dir = base_dir / sku
        
        # Check if the directory already exists, maybe we have duplicate SKU as Etsy allows that
        if sku_dir.exists():
            # Append the current datetime to create a unique directory name, ex: 11_20240227_200501
            datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            sku_dir = base_dir / f"{sku}_{datetime_str}"
        
        # Create the directory
        sku_dir.mkdir(parents=True, exist_ok=True)
        
        # Download each image for the current row
        for i in range(1, 11):
            image_url = row.get(f'IMAGE{i}', None)
            download_image(image_url, sku_dir, i)

    print("All images have been downloaded.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
    else:
        file_path = sys.argv[1]
        main(file_path)
#EOF