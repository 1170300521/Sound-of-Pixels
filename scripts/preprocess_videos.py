"""
Preprocess videos from youtube to get audios and images
"""

import os
import os.path as osp
import cv2
import moviepy.editor as mp

video_root = "./data/video"
audio_root = "./data/audio"
frame_root = "./data/frames"


def get_frames(instr, video, fps=8):
    """
    extract frames from video
    """
    cap = cv2.VideoCapture(osp.join(video_root, instr, video))
    i = 0
    count = 1
    img_path = osp.join(frame_root, instr, video)
    if not osp.exists(img_path):
        os.makedirs(img_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i >= fps - 1:
            img_name = (6 - len(str(count)))*'0' + str(count) + '.jpg'
            cv2.imwrite(osp.join(img_path, img_name))
            count += 1
            i = 0
            continue
        i += 1
    cap.release()
    cv2.destoryAllWindows()


def get_audio(instr, video, hz=11025):
    """
    Extract audio from video
    """
    audio_path = osp.join(audio_root, instr)
    if not osp.exists(audio_path):
        os.makedirs(audio_path)
    audio_name = video.split(".")[0] + ".mp3"
    clip = mp.VideoFileClip(osp.join(video_root, instr, video))
    clip.audio.write_audiofile(osp.join(audio_path, audio_name))
    

def main():
    for instr in video_root:
        for video in instr:
            get_frames(instr, video)
            get_audio(instr, video)
        print("Complete " + instr)
    print("Complete datset preprocessing!")


if __name__ == "__main__":
    main()
