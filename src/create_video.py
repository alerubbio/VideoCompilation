import os
import json
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, vfx, TextClip

PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
PATH_TO_RAW_CLIPS = 'VideoCompilation\VideoFiles\\raw_clips'
FONT_PATH = 'E:\Projects\TwitchMontage\VideoCompilation\Fonts\Twitchy.TV Font\Twitchy.TV.ttf'
def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    list = file.readlines()
    return list
    
def get_clip_data(filename):
    file = open('VideoCompilation\ClipData\clips_data.json')
    clips_data = json.load(file)

    return clips_data[filename]

def create_clips(list):
    clips = []
    for filename in list:
        filename = filename.strip()
        video_file_path = os.path.join(PATH_TO_RAW_CLIPS, filename)

        clip = VideoFileClip(video_file_path)
        clip = clip.fx(vfx.fadein, .1).fx(vfx.fadeout, .15)
        clip = add_text_overlay(clip, filename)

        clips.append(clip)

    return clips

def create_draft(clips):
    draft = concatenate_videoclips(clips, method='compose')
    draft.write_videofile("VideoCompilation/VideoFiles/videos/draft.mp4")
    return draft

def add_text_overlay(clip, file):
    clip_data = get_clip_data(file)
    streamerName = str(clip_data.get('streamerName'))

    text_clip = TextClip(txt = streamerName, size = (400,0), color = "blue")
    tc_width, tc_height = text_clip.size

    text_clip = text_clip.set_position(0, tc_height)
    text_clip = text_clip.set_start((0,0))
    text_clip = text_clip.set_duration(2.5)
    text_clip = text_clip.crossfadein(0.5).crossfadeout(0.5)
    clip = CompositeVideoClip([clip, text_clip])
    return clip

def create_movie():
    list = read_valid_clips_list()
    clips = create_clips(list)
    draft = create_draft(clips)

    return draft
    
movie = create_movie()

