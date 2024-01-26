# Etsy to WooCommerce Image Downloader

This script facilitates the migration of product images from Etsy to WooCommerce by automating the download and organization of images based on the SKU.

## Brief Overview

When expanding an online store from Etsy to WooCommerce, one of the more time-consuming tasks is transferring the product images. This script takes an exported CSV file from Etsy, which contains the product SKUs and image URLs, and downloads all associated images into neatly organized folders named by SKU for easy upload to WooCommerce.

## Blog Post

For a detailed account of why and how this script was created, you can read my personal experience on my blog post: [Migrating Etsy Listings to WooCommerce](https://www.mazensenih.com/blog/how-i-effortlessly-migrated-my-etsy-listings-to-woocommerce)

## Prerequisites

Before running the script, you need to have Python installed on your system. Additionally, a few Python packages are required:

- pandas: For reading the CSV file and handling data.
- requests: To download images from the internet.
- openpyxl: To allow pandas to work with Excel files.

Ensure these packages are installed by running the following command:

```sh
pip install -r requirements.txt
```

This command will install all the necessary dependencies listed in the requirements.txt file included in this repository.

## Installation

To set up the script on your local machine, follow these steps:

1. Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/MazenSenih/EtsyShopExportImagesDownloader.git
```

2. Navigate to the repository directory:

```sh
cd EtsyShopExportImagesDownloader
```

3. Install the required dependencies using:

```sh
pip install -r requirements.txt

or 

pip3 install -r requirements.txt
```

## Usage

To use the script, you'll need to have your Etsy CSV file ready. Here's how to run the script:

1. Download and place the `EtsyListingsImages.csv` file in the root directory of the cloned repository. 

For more info about obtaining your shop's listing csv: https://help.etsy.com/hc/en-us/articles/360000343508-How-to-Download-Your-Listing-Information?segment=selling

2. Run the script using Python:

```sh
python3 etsy_image_downloader.py
```

The script will create a directory named etsy_images containing subdirectories for each SKU. Each subdirectory will contain the downloaded images.

## Configuration

The script is designed to work with a specific format of the Etsy CSV file. Ensure your CSV file has the following columns:
- SKU: Unique identifier for each product.
- IMAGE1, IMAGE2, ..., IMAGE10: Columns containing the URLs of product images.

You can modify the script to accommodate different CSV structures or additional columns as needed.

## Contributing

Contributions to improve this script or add more features are welcome. If you have suggestions or improvements, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

A big shoutout to the Etsy community and WooCommerce developers for making online selling a breeze. This script is a small contribution to help streamline the process for store owners expanding their digital presence.

## Support

For any queries or issues with running the script, feel free to open an issue in this repository or contact me directly through my [website](https://mazensenih.com).

Remember to check out the detailed story of this script's creation and its practical application on my [blog post](https://www.mazensenih.com/blog/how-i-effortlessly-migrated-my-etsy-listings-to-woocommerce).

Happy selling!

[Mazen Alsenih](https://mazensenih.com)
