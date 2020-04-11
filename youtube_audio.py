from __future__ import unicode_literals
import youtube_dl
import os

# os.chdir("/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded")


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def download_audio(youtube_link,download_directory,file_name):
    # os.chdir(download_directory)
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': download_directory+file_name,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])



# download_audio("https://www.youtube.com/watch?v=dGIaLcgjb0I","/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded","abcd")
