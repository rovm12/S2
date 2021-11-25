

import os


def motion_vectors():
    # command to extract and save a video with motion vectors
    terminal_command = "ffmpeg -flags2 +export_mvs -i vid2.mp4 -vf codecview=mv=pf+bf+bb motion_vectors.mp4"
    os.system(terminal_command)


if __name__ == '__main__':
    motion_vectors()