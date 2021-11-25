import os

from moviepy.editor import *


def cut_from_beg(N, file, name_cut):
    # loading video dsa gfg intro video
    clip = VideoFileClip(file)

    # getting only first 5 seconds
    clip = clip.subclip(0, N)

    clip.write_videofile(name_cut)
    print("cut_from_beg done it\n")


def extract_audio():
    # export audio as stereo track in mp3
    terminal_command = "ffmpeg -i bbb.mp4 -vn -ar 44100 -ac 2 -ab 192k -f mp3 audio1.mp3"
    os.system(terminal_command)
    print("extract_audio done it\n")


def aac():
    # command to export audio in AAC w/ lower bit rate
    terminal_command = "ffmpeg -i audio1.mp3 -c:a libfdk_aac -b:a 128k audio2.m4a"
    os.system(terminal_command)
    print("aac done it\n")


def merge1():
    # command to merge both audio files and the video
    terminal_command = "ffmpeg -i vid2.mp4 -i audio1.mp3 -i audio2.m4a final_vid.mp4"
    os.system(terminal_command)
    print("merge1 done it")


if __name__ == '__main__':
    cut_from_beg(60, "bbb.mp4", "vid2.mp4")
    extract_audio()
    aac()
    merge1()