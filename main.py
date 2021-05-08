from __future__ import unicode_literals
from youtubesearchpython import *
from tkinter import *
import tkinter as tk
import downloader
from tkinter import filedialog
import sys
import os


def downloadSongs(path):
    strings = songTextArea.get('1.0', 'end-1c').splitlines()
    for element in strings:
     videosSearch = VideosSearch(element, limit=1)
     if(v.get()==1):
      downloader.downloadSong(videosSearch.result()['result'][0]['link'], path)
     else:
      downloader.downloadSong(element,path)







def browse_directory():
    parentDirName = filedialog.askdirectory()
    directoryText.replace('1.0', 'end-1c', parentDirName)
    create_path()


def create_path():
    parentDirName = directoryText.get('1.0', 'end-1c')
    mixtapeName = mixtapeEntry.get()
    fullPath = parentDirName + '/' + mixtapeName
    directoryText.replace('1.0', 'end-1c', fullPath)
    if not (os.path.isdir(fullPath)):
        os.mkdir(fullPath)


class PrintLogger:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(tk.END, text)


    def flush(self):
        pass


root = Tk()
root.title("Yotube MP3 Downloader")
w=500
h=550
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.maxsize(500, 550)
root.minsize(500, 550)
root.columnconfigure(0, weight=1)
enterSongsLabel = Label(root, text="Enter songs/URL:")
enterSongsLabel.grid()

songTextArea = Text(height=10, width=50)
songTextArea.grid()
v = tk.IntVar()
tk.Radiobutton(root,
               text="Song",
               padx = 20,
               variable=v,
               value=1).grid()

tk.Radiobutton(root,
               text="URL",
               padx = 20,
               variable=v,
               value=2).grid()
v.set(1)
mixtapeLabel = Label(root, text="Choose mixtape name:")
mixtapeLabel.grid()
mixtapeEntry = Entry(root)
mixtapeEntry.grid()
directoryLabel = Label(root, text="Choose directory:")
directoryLabel.grid()
directoryButton = Button(text="Browse", command=lambda: browse_directory())
directoryButton.grid()
directoryText = Text(root, width=50, height=1)
directoryText.grid(pady=8)


downloadButton = Button(text="Download", command=lambda: downloadSongs(directoryText.get('1.0', 'end-1c')))
downloadButton.grid(pady=8)
logArea = Text(height=7, width=50)
logArea.grid()
pl = PrintLogger(logArea)

sys.stdout = pl

root.mainloop()
