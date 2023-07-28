import os
from pytube import YouTube

def youtubemp4downloader(download_path):
    # user url input
    yt = YouTube(str(input("\n Enter the URL of the video you want to download: \n>> ")))

    # resolution
    video = yt.streams.filter(res="720p").first()

    # download file
    out_file = video.download(output_path=str(download_path))

    # save file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")

    # recurse / repeat
    youtubemp4downloader(download_path)

youtubemp4downloader(download_path="C:\Videos")
