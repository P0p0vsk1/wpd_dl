WatchPeopleDie Scraper
======================

This script allows you to extract and download `.mp4` links from WatchPeopleDie.tv, a website that contains graphic content.

Requirements
------------

This script requires the following libraries to be installed:

-   cfscrape
-   BeautifulSoup
-   requests
-   tqdm

You can install these libraries using `pip`.

Usage
-----

To use this script, save it to your local machine and run the following command:

python

```
python wpd_dl.py

```

You will be prompted to enter the category and number of pages you want to scrape.

The script will then extract all `.mp4` links from the specified pages and prompt you to download them. If you choose to download the files, they will be saved in a new directory named `wpd_{category}_{pages}`. If the directory already exists, the files will be saved in it instead.

If you choose not to download the files, the script will save the links to a text file named `wpd_{category}_{pages}.txt`.

Disclaimer
----------

The content on WatchPeopleDie.tv can be graphic and disturbing. Please use this script at your own risk and discretion. The author of this script takes no responsibility for any use or misuse of this script.