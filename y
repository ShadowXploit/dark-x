import pytube
import os
def download_video(url, resolution_choice):
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        stream.download('/storage/emulated/0/')
        print("  \033[1;31m[\033[1;36m+\033[1;31m] \033[1;36mVideo saved in internal memory!")
    else:
        print("\033[1;31mVideo with the selected resolution is not available.")
video_link = input("  \033[1;31m[\033[1;36m+\033[1;31m] \033[1;34mYouTube video link \033[1;31m: \033[1;37m")
print("\n  \033[1;31m[\033[1;37m1\033[1;31m] \033[1;36m144p\n  \033[1;31m[\033[1;37m2\033[1;31m] \033[1;36m240p\n  \033[1;31m[\033[1;37m3\033[1;31m] \033[1;36m360p\n  \033[1;31m[\033[1;37m4\033[1;31m] \033[1;36m720p\n  \033[1;31m[\033[1;37m5\033[1;31m] \033[1;36m1080p\n")
resolution_choice = input("  \033[1;31m[\033[1;36m+\033[1;31m] \033[1;34mChoose resolutions \033[1;31m: \033[1;37m")
print("")
resolutions = {'1': '144p', '2': '240p', '3': '360p', '4': '720p', '5': '1080p'}
if resolution_choice in resolutions:
    resolution = resolutions[resolution_choice]
    download_video(video_link, resolution)
else:
    print("\033[1;31mInvalid resolution!!")
    exit()