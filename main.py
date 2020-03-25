import pytube
from pytube import YouTube
import moviepy.editor as mp
import tkinter
import tkinter.messagebox
from tkinter import filedialog
from tkinter import *
import os
# Crear la ventana
top = tkinter.Tk()
top.title("YouTube Downloader | Santy Alvarez")
top.geometry("720x520")
# Funcion para descargar el video
def downloadVideo():
    try:
        video_url = url_video.get()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        folder = folderPath.get()
        video.download(folder)
        tkinter.messagebox.showinfo("Video descargado", "Video descargado con exito")
    except:
        tkinter.messagebox.showerror("Error en la descarga", "Ha habido un error en la descarga del video")

def downloadAudio():
    try:
        video_url = url_video.get()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        name = YouTube(video_url)
        folder = folderPath.get()
        video.download(folder)
        os.chdir(folder)
        mp4name = str(name.title)+".mp4"
        mp3name = str(name.title)+".mp3"
        clip = mp.VideoFileClip(mp4name)
        clip.audio.write_audiofile(mp3name)
        try:
            del clip.reader
            del clip
            os.remove(mp4name)
        except:
            print("No existe el fichero")
        tkinter.messagebox.showinfo("Audio descargado", "Audio descargado con exito")
    except:
        tkinter.messagebox.showerror("Error en la descarga", "Ha habido un error en la descarga del audio")

def setDirectory():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)

downloadVid = tkinter.Button(top, text="Descargar video", command = downloadVideo).place(x=200,y=100)
downloadAud = tkinter.Button(top, text="Descargar audio", command = downloadAudio).place(x=400,y=100)
folderPath = StringVar()
saveDirectory = tkinter.Button(top, text="¿Donde guardarlo?", command = setDirectory).place(x=420,y=50)
tkinter.Label(top, text="URL del video").place(x=200,y=50)
url_video = tkinter.Entry(top)
url_video.place(x=280,y=50)
top.mainloop()
