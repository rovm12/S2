from class_S2 import VideoCodec


if __name__ == '__main__':
    value = input("Type what option do you want form 1 to 4 (in the order that appears on Seminar 2 slides): ")
    if value == "1":
        VideoCodec.motion_vectors()

    elif value == "2":
        VideoCodec.cut_from_beg(60, "bbb.mp4", "vid2.mp4")
        VideoCodec.extract_audio()
        VideoCodec.aac()
        VideoCodec.merge1()

    elif value == "3":
        VideoCodec.broadcast_std()

    elif value == "4":
        VideoCodec.add_sub()

    else:
        print("That was never an option. :( ")


