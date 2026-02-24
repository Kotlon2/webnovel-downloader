# webnovel-downloader
A multithreaded Python web scraping tool that downloads novel chapters as text files, combined with a Tkinter-based fullscreen reader for structured, chapter-by-chapter viewing.

--------------------
# Features

- Scrape chapters from a WebNovel website automatically.
- Saves each chapter as a separate `.txt` file in a folder of your choice.
- GUI reader allows you to scroll through chapters and navigate using:
  - Arrow keys (Up/Down for scroll, Left/Right for previous/next chapter)
  - Buttons for previous and next chapters
- Dark mode GUI for comfortable reading.

---------------------

## Installation

# Clone this repository:
```bash
git clone https://github.com/Kotlon2/webnovel-downloader.git


#Navigate into the project folder:
cd webnovel-downloader

#Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

#Install dependencies:
pip install -r requirements.txt

---------------------
## Usage 

#Open webnovel-downloader
#Change the URL to the desired url
#Adjust the range of chapter to be downloaded

#Run the scraper to download chapters:
python webnovel-downloader.py

#You will be prompted to select where you want the files to be downloaded

## Reader

#Run the GUI reader to view downloaded chapter:

WebNovelGUI.py

#You will be prompted to select the folder containing the .txt files
#Use arrow keys to navigate

#This project is licensed under the MIT License, See the LICENSE file for details.

---------------------

## DISCLAIMER

-This tool is intended for personal use and educational purposes only.
-Users must comply with the Terms of Service of the websites they scrape.
-Do not use this tool to overwhelm or attack websites (DDos or excessive requests).
-The author is not responsible for any misuse of this software. 
