# read in list of valid clips
# concat them
# edit them

from moviepy.editor import VideoFileClip, concatenate_videoclips

PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
PATH_TO_RAW_CLIPS = 'VideoCompilation\VideoFiles\\raw_clips\\'

def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    list = file.readlines()
    return list

def create_clips_from_list(list):
    clips = []
    for item in list:
        clip = VideoFileClip(str(PATH_TO_RAW_CLIPS) + str(item))
        clips.append(clip)

    return clips


def create_draft(clips):
    draft = concatenate_videoclips(clips)
    draft.write_videofile("VideoCompilation/VideoFiles/videos/draft.mp4")
    return draft

list = read_valid_clips_list()
clips = create_clips_from_list(list)
draft = create_draft(clips)