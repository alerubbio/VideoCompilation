import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
PATH_TO_RAW_CLIPS = 'VideoCompilation\VideoFiles\/raw_clips'

def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    list = file.readlines()
    return list

def create_clips_from_list(list):
    clips = []
    for filename in list:
        video_file_path = os.path.join(PATH_TO_RAW_CLIPS, filename.strip())

        clip = VideoFileClip(video_file_path)
        clips.append(clip)

    return clips

def create_draft(clips):
    draft = concatenate_videoclips(clips, method='compose')
    draft.write_videofile("VideoCompilation/VideoFiles/videos/draft.mp4")
    return draft

list = read_valid_clips_list()
clips = create_clips_from_list(list)
draft = create_draft(clips)
