from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(save_path)
        print('Video Downloaded Successfully')
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder:{folder}")
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    save_path = open_file_dialog()


    download_video('https://www.youtube.com/watch?v=9bZkp7q19f0', 'C:/Users/HP/Downloads')