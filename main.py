from yt_dlp import YoutubeDL

url = input("url:")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "./musics/%(title)s.%(ext)s",
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])