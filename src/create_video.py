import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
PATH_TO_RAW_CLIPS = 'E:\Projects\TwitchMontage\VideoCompilation\VideoFiles\\raw_clips'

def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    list = file.readlines()
    return list

def create_clips_from_list(list):
    clips = []
    for filename in list:
        video_file_path = os.path.abspath(os.path.join(PATH_TO_RAW_CLIPS, filename))
        clip = VideoFileClip(str(video_file_path))
        clips.append(clip)

    return clips

def create_draft(clips):
    draft = concatenate_videoclips(clips)
    draft.write_videofile("VideoCompilation/VideoFiles/videos/draft.mp4")
    return draft

# list = read_valid_clips_list()
# clips = create_clips_from_list(list)
# draft = create_draft(clips)


clip1 = VideoFileClip('VideoCompilation\VideoFiles\\raw_clips\clip0.mp4')
clip2 = VideoFileClip('VideoCompilation\VideoFiles\\raw_clips\clip1.mp4')
combined = concatenate_videoclips([clip1, clip2])
combined.write_videofile("VideoCompilation/VideoFiles/videos/draft.mp4")
