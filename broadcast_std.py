import os


def broadcast_std():
    # it prints the information we want: in this case, broadcast standard and other information related
    terminal_command = "ffprobe -v quiet -print_format json -show_format -show_streams bbb.mp4"
    os.system(terminal_command)


if __name__ == '__main__':
    broadcast_std()