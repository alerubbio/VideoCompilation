from cgitb import text
import os
import json
from turtle import bgcolor
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, concatenate_videoclips, vfx, TextClip

PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
PATH_TO_RAW_CLIPS = 'VideoCompilation\VideoFiles\\raw_clips'
FONT_PATH = 'E:\Projects\TwitchMontage\VideoCompilation\Fonts\Twitchy.TV Font\Twitchy.TV.ttf'

# reads clip valid clip names from file
def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    valid_list = file.readlines()
    return valid_list

# gets clip data
def get_clip_data(filename):
    file = open('VideoCompilation\ClipData\clips_data.json')
    clips_data = json.load(file)

    return clips_data[filename]

def create_clips(clip_list):
    clips = []
    texts = []
    currentTotalDuration = 0
    for filename in clip_list:
        filename = filename.strip()
        clip_data = get_clip_data(filename)
        video_file_path = os.path.join(PATH_TO_RAW_CLIPS, filename)

        current_clip_duration = float(clip_data['clipDuration'])
        
        # create video clip
        clip = VideoFileClip(video_file_path).resize((1920, 1080))
        clip = clip.set_duration(current_clip_duration)
        clip = clip.fx(vfx.fadein, .1).fx(vfx.fadeout, .1)

        # create text overlay for clip
        text_overlay = create_text_overlay(clip_data, currentTotalDuration)
        
        # combine clip and text before concatenation
        clip = CompositeVideoClip([clip, text_overlay]).set_duration(current_clip_duration)
        currentTotalDuration += current_clip_duration

        texts.append(text_overlay)
        clips.append(clip)

    return clips, texts, currentTotalDuration

def create_text_overlay(clip_data, currentDuration):
    streamerName = str(clip_data.get('streamerName'))

    text_clip = TextClip(txt = streamerName, font = FONT_PATH, size = (300,0), color = 'rgb(145, 70, 255)')
    tc_width, tc_height = text_clip.size
    
    text_clip = text_clip.set_start(0)
    text_clip = text_clip.set_position('center')
    text_clip = text_clip.set_duration(2.5)
    text_clip = text_clip.crossfadein(0.2).crossfadeout(0.5)

    color_clip = ColorClip(size=(tc_width + 5, tc_height + 5), color='white').set_opacity(.6)
    final_clip = CompositeVideoClip([color_clip, text_clip]).set_position(('left', 'bottom'))

    return final_clip

def create_final_video(clips, texts, totalDuration):
    final_movie = concatenate_videoclips(clips, method='compose').set_duration(totalDuration) # use method='chain'
    return final_movie

def create_movie():
    valid_list = read_valid_clips_list()
    clips, texts, totalDuration = create_clips(valid_list)
    movie = create_final_video(clips, texts, totalDuration)
    
    return movie

movie = create_movie()
movie.write_videofile('VideoCompilation\VideoFiles\\videos\movie.mp4', threads = 8, verbose=False, logger=None, preset='ultrafast')
