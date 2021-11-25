import os


def broadcast_std():
    # it prints
    terminal_command = "ffprobe -v quiet -print_format json -show_format -show_streams bbb.mp4"
    os.system(terminal_command)


if __name__ == '__main__':
    broadcast_std()