import cfscrape
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import os

mp4_links = []

category = input("Enter the category you want: ")
pages = input("How many pages? ")

if int(pages) == 1:
    url = f"https://watchpeopledie.tv/h/{category}?page=1"
    scraper = cfscrape.CloudflareScraper()
    req = scraper.get(url).content
    soup = BeautifulSoup(req, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        if str(href).endswith(".mp4"):
            mp4_links.append(href)
else:
    for page in range(1, int(pages)):
        url = f"https://watchpeopledie.tv/h/{category}?page={page}"
        scraper = cfscrape.CloudflareScraper()
        req = scraper.get(url).content
        soup = BeautifulSoup(req, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if str(href).endswith(".mp4"):
                mp4_links.append(href)

if len(mp4_links) > 0:
    print("[INFO] MP4 links extracted!")
    choice = input("Should I download them (y/n)? ")
    if choice == "y" or choice == "Y":
        if not os.path.exists(f"wpd_{category}_{pages}"):
            os.mkdir(f"wpd_{category}_{pages}")
        os.chdir(f"wpd_{category}_{pages}")
        for link in mp4_links:
            filename = link.split("/")[-1]
            response = requests.get(link, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            with open(filename, "wb") as f:
                with tqdm(total=total_size, unit="iB", unit_scale=True) as progress_bar:
                    for data in response.iter_content(block_size):
                        f.write(data)
                        progress_bar.update(len(data))
            print("Downloaded file:", filename)
    else:
        print("[INFO] Download aborted. saving links to a text file...")
        file = open(f"wpd_{category}_{pages}.txt", 'w')
        for link in mp4_links:
            file.write(link + "\n")
        file.close()
else:
    print("[DEBUG]: " + str(mp4_links))