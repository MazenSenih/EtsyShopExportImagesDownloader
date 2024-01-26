# This script will help you to download the Etsy images from your shop's export csv into SKU folders
# Script author: Mazen Alsenih (mazensenih.com | mazen.el.senih@gmail.com)
# Hope it helps you. 😉

# Libraries
import os
import requests
import pandas as pd
from pathlib import Path
##

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

# Replace 'EtsyListingsImages.xlsx' with the path to your Excel file
file_path = 'EtsyListingsImages.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Iterate through each row in the DataFrame
for _, row in df.iterrows():
    # Get the SKU and create a directory for it
    sku = str(row['SKU'])
    sku_dir = Path('etsy_images') / sku
    sku_dir.mkdir(parents=True, exist_ok=True)
    
    # Download each image for the current row
    for i in range(1, 11):
        image_url = row.get(f'IMAGE{i}', None)
        download_image(image_url, sku_dir, i)

print("All images have been downloaded.")

#####
