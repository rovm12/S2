import os


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


if __name__ == '__main__':
    motion_vectors()