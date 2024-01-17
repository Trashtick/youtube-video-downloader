from pytube import YouTube
import tqdm
def downloader(link):
    k = YouTube(link)
    a= k.streams.get_highest_resolution()
    a.download()
    print("download is successful")
link= input("enter: ")
downloader(link)