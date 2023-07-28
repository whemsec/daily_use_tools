import os
from pytube import YouTube

def youtubemp3downloader(download_path):
    # user url input
    yt = YouTube(str(input("\n Enter the URL of the video you want to download: \n>> ")))

    # extract audio
    video = yt.streams.filter(only_audio=True).first()

    # download file
    out_file = video.download(output_path=str(download_path))

    # save file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded.")

    # recurse / repeat
    youtubemp3downloader(download_path)

youtubemp3downloader(download_path="C:\Youtube")
