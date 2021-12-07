import os
from moviepy.editor import *


class VideoCodec:

    # PRINTING MOTION VECTORS
    @staticmethod
    def motion_vectors():
        men = input("Type 1 for Macro Blocks information and 2 gor motion vectors: ")
        if men == "1":
            # Write macroblocks information into a .txt script
            terminal_command1 = "ffmpeg -debug mb_type -i bbb.mp4 out.mp4 2> macroblocks.txt"
            os.system(terminal_command1)
        elif men == "2":
            # Command to extract and save a video with motion vectors
            terminal_command = "ffmpeg -flags2 +export_mvs -i bbb.mp4 -vf codecview=mv=pf+bf+bb motion_vectors.mp4"
            os.system(terminal_command)

    # CREATING CONTAINER
    @staticmethod
    def cut_from_beg(N, file, name_cut):
        # loading video dsa gfg intro video
        clip = VideoFileClip(file)

        # getting only first 5 seconds
        clip = clip.subclip(0, N)

        clip.write_videofile(name_cut)
        print("cut_from_beg done it\n")

    @staticmethod
    def extract_audio():
        # export audio as stereo track in mp3
        terminal_command = "ffmpeg -i bbb.mp4 -vn -ar 44100 -ac 2 -ab 192k -f mp3 audio1.mp3"
        os.system(terminal_command)
        print("extract_audio done it\n")

    @staticmethod
    def aac():
        # command to export audio in AAC w/ lower bit rate
        terminal_command = "ffmpeg -i audio1.mp3 -c:a libfdk_aac -b:a 128k audio2.m4a"
        os.system(terminal_command)
        print("aac done it\n")

    @staticmethod
    def merge1():
        # command to merge both audio files and the video
        terminal_command = "ffmpeg -i vid2.mp4 -i audio1.mp3 -i audio2.m4a final_vid.mp4"
        os.system(terminal_command)
        print("merge1 done it")

    # STANDARD BROADCAST
    @staticmethod
    def broadcast_std():
        # it prints the information we want: in this case, broadcast standard and other information related
        terminal_command = "ffprobe -v quiet -print_format json -show_format -show_streams bbb.mp4"
        os.system(terminal_command)

    # SUBTITLES
    @staticmethod
    def add_sub():
        #read the .txt with the subtitles
        terminal_command = "ffmpeg -i bbb_subtitles.srt subtitles.ass"
        os.system(terminal_command)

        # merge the subtitles with the video to see them on screen
        terminal_command2 = "ffmpeg -i bbb.mp4 -vf ass=subtitles.ass subtitled_bbb.mp4"
        os.system(terminal_command2)


