import cloudscraper
import os
from bs4 import BeautifulSoup
import certifi
from concurrent.futures import ThreadPoolExecutor
import time
import random
import tkinter as tk
from tkinter import filedialog
session = cloudscraper.create_scraper()

headers ={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }

root = tk.Tk()
root.withdraw()

OUTPUT_FOLDER = filedialog.askdirectory(title="Select Folder to Save Chapters")

root.destroy()

if not OUTPUT_FOLDER:
    print("No folder selected. Exiting.")
    exit()
    
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def scrape_chapter(chapter_num):
    
        url = f"https://example/example/example/example-{chapter_num}/" # Change this URL to the webnovel chapter URL pattern you want to scrape, make sure to include the chapter number in the URL pattern as shown.
        
        response = session.get(url, headers=headers)
        
        print(f"Scraping chapter {chapter_num} from {url} - Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Failed to retrieve chapter {chapter_num}. Status code: {response.status_code}")
            return
                
        soup = BeautifulSoup(response.content, "html.parser")
   
        title = soup.select_one(".novel-title")
        
        h1= soup.select_one('h1')
        
        chapter = soup.find("div", id ="chr-content")
        
        if chapter:
            paragraphs = chapter.find_all("p")
            
            with open(os.path.join(OUTPUT_FOLDER, f"chapter_{chapter_num}.txt"), "w", encoding="utf-8") as f:
                f.write(title.text + "\n\n")
                f.write("=" * len(title.text) + "\n\n")
                
                f.write(h1.text + "\n\n")
                f.write("-" * len(h1.text) + "\n\n") 
                               
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if text:
                        f.write(text + "\n\n")
        else:
            print(f"Chapter {chapter_num} not found. Stopping.")
            
            
def scrape():
    for chapter_num in range(1, 5):
        scrape_chapter(chapter_num)
        time.sleep(random.uniform(1, 3)) #CLOUD FLARE IS SENSITIVE TO RAPID REQUESTS, SO WE ADD A RANDOM DELAY BETWEEN 1 AND 3 SECONDS TO AVOID GETTING BLOCKED. THIS IS SLOW, BUT IT HELPS TO ENSURE THAT THE SCRAPER CAN CONTINUE TO WORK WITHOUT BEING BLOCKED BY CLOUD FLARE. YOU CAN ADJUST THE DELAY TIME AS NEEDED, BUT KEEP IN MIND THAT SHORTER DELAYS MAY INCREASE THE RISK OF GETTING BLOCKED.

        
if __name__ == "__main__":
    scrape()
    