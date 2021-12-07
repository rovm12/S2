import os


def add_sub():
    # command that read the subtitles.srt file and convert it to format .ass
    terminal_command = "ffmpeg -i bbb_subtitles.srt subtitles.ass"
    os.system(terminal_command)

    # command to add the subtitle to the video
    terminal_command2 = "ffmpeg -i bbb.mp4 -vf ass=subtitles.ass subtitled_bbb.mp4"
    os.system(terminal_command2)


if __name__ == '__main__':
    add_sub()


