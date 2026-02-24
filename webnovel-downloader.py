import requests 
import os
from bs4 import BeautifulSoup
import certifi
from concurrent.futures import ThreadPoolExecutor
import time
import random
import tkinter as tk
from tkinter import filedialog
session = requests.Session()

headers ={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
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
    
        url = f"https://example.com/example/chapter/{chapter_num}/" # Change this URL to the webnovel chapter URL pattern you want to scrape, make sure to include the chapter number in the URL pattern as shown.
        
        response = session.get(url, headers=headers, verify=certifi.where())
        
        print(f"Scraping chapter {chapter_num} from {url} - Status Code: {response.status_code}")
        
        if response.status_code != 200:
            print(f"Failed to retrieve chapter {chapter_num}. Status code: {response.status_code}")
            return
        
        time.sleep(random.uniform(0.05, 0.15))
        
        soup = BeautifulSoup(response.content, "html.parser")
   
        title = soup.select_one(".novel-title")
        
        h1= soup.select_one('h1')
        
        chapter = soup.find("div", id ="chapterText")
        
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
    with ThreadPoolExecutor(max_workers=3) as executor: # Adjust max_workers based on your system capabilities and the website's rate limits. DO NOT GO TOO HIGH TO AVOID GETTING BLOCKED BY THE WEBSITE. STAY WITHIN A REASONABLE NUMBER OF WORKERS. LIKE 3 OR 4 WORKERS TOPS.
        chapter_nums = range(1, 5) # Change this range to the number of chapters you want to scrape, set it one higher than the last chapter number you want to scrape.
        executor.map(scrape_chapter, chapter_nums)

        
if __name__ == "__main__":
    scrape()
    