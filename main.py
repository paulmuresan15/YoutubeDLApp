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
        downloader.download(videosSearch.result()['result'][0]['link'], path)


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


class PrintLogger:  # create file like object
    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text)  # write text to textbox
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


root = Tk()
root.title("Downloader")
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)
root.columnconfigure(0, weight=1)
enterSongsLabel = Label(root, text="Enter songs:")
enterSongsLabel.grid()

songTextArea = Text(height=10, width=50)
songTextArea.grid()
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

# mixtapeEntry.grid()

downloadButton = Button(text="Download", command=lambda: downloadSongs(directoryText.get('1.0', 'end-1c')))
downloadButton.grid(pady=8)
logArea = Text(height=7, width=50)
logArea.grid()
pl = PrintLogger(logArea)

sys.stdout = pl

root.mainloop()