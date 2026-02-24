import os 
import re
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

chapter_folder = filedialog.askdirectory(title="Select Chapter Folder")

root.destroy()

if not chapter_folder:
    print("No folder selected. Exiting.")
    exit()

chapters = ([f for f in os.listdir(chapter_folder) if f.endswith(".txt")])

chapters.sort(key=lambda x: int(re.search(r'\d+', x).group(0)))

current = 0

def load_chapter(index):
    
    if 0 <= index < len(chapters):
        with open(os.path.join(chapter_folder, chapters[index]), "r", encoding="utf-8") as f:
            content = f.read()
        text_box.config(state="normal")
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, content)
        text_box.config(state="disabled")
        chapter_label.config(text=f"{chapters[index]} ({index + 1}/{len(chapters)})")
        
        
def next_chapter():
    global current
    if current < len(chapters) - 1:
        current += 1
        load_chapter(current)
        
def prev_chapter():
    global current
    if current > 0:
        current -= 1
        load_chapter(current)
        
root = tk.Tk()
root.title("Web Novel Reader")

root.attributes("-fullscreen", True)

root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

root.config(bg="black")


text_box = tk.Text(
    root,
    bg="#1e1e1e", # Change this to your preferred background color
    fg="#ffffff", # Change this to your preferred text color
    wrap=tk.WORD,
    font=("Times New Roman", 14),
    padx=20,
    pady=20
)
text_box.pack(expand=True, fill=tk.BOTH)
text_box.config(state="disabled")

def scroll_up(event):
    text_box.yview_scroll(-1, "units")
    return "break"
def scroll_down(event):
    text_box.yview_scroll(1, "units")
    return "break"
text_box.bind("<Up>", scroll_up)
text_box.bind("<Down>", scroll_down)

def next_chapter_key(event):
    next_chapter()
    return "break"
def prev_chapter_key(event):
    prev_chapter()
    return "break"
text_box.bind("<Right>", next_chapter_key)
text_box.bind("<Left>", prev_chapter_key)

chapter_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
chapter_label.pack(pady=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=5)

prev_button = tk.Button(button_frame, text="Previous", command=prev_chapter)
prev_button.pack(side="left", padx=5)

next_button = tk.Button(button_frame, text="Next", command=next_chapter)
next_button.pack(side="left", padx=5)

load_chapter(current)

root.mainloop()