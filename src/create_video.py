import os
import json
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, concatenate_videoclips, vfx, TextClip

PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
PATH_TO_RAW_CLIPS = 'VideoCompilation\VideoFiles\\raw_clips'
FONT_PATH = 'E:\Projects\TwitchMontage\VideoCompilation\Fonts\Valorant Font.ttf'
PATH_TO_INTRO = 'E:\Projects\TwitchMontage\VideoCompilation\VideoFiles\\videos\YT_VALORANT_INTRO.mp4'

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
    clips = [VideoFileClip(PATH_TO_INTRO).resize((1920, 1080)).set_fps(30)]
    texts = []
    currentTotalDuration = 0
    for filename in clip_list:
        filename = filename.strip()
        clip_data = get_clip_data(filename)
        video_file_path = os.path.join(PATH_TO_RAW_CLIPS, filename)

        current_clip_duration = float(clip_data['clipDuration'])
        
        # create video clip
        clip = VideoFileClip(video_file_path).resize((1920, 1080)).set_fps(30)
        clip = clip.set_duration(current_clip_duration)
        clip = clip.fx(vfx.fadein, .1).fx(vfx.fadeout, .1)

        # create text overlay for clip
        text = create_text_overlay(clip_data, currentTotalDuration)
        
        # combine clip and text before concatenation
        clip = CompositeVideoClip([clip, text]).set_duration(current_clip_duration)
        currentTotalDuration += current_clip_duration

        texts.append(text)
        clips.append(clip)

    return clips, texts, currentTotalDuration

def create_text_overlay(clip_data, currentDuration):
    streamerName = str(clip_data.get('streamerName'))
    clip_duration = int(clip_data.get('clipDuration'))

    text_clip = TextClip(txt = streamerName, font = FONT_PATH, size = (0,75), color = 'rgb(202, 105, 255)')
    tc_width, tc_height = text_clip.size
    
    text_clip = text_clip.set_start(0)
    text_clip = text_clip.set_position( (20, 900) )
    text_clip = text_clip.set_duration(min([clip_duration / 3, 6]))
    text_clip = text_clip.crossfadein(0.2).crossfadeout(0.5)

    return text_clip

def create_final_video(clips, texts, totalDuration):
    final_movie = concatenate_videoclips(clips, method='chain').set_duration(totalDuration) 
    return final_movie

def create_movie():
    valid_list = read_valid_clips_list()
    clips, texts, totalDuration = create_clips(valid_list)
    movie = create_final_video(clips, texts, totalDuration)
    
    return movie


movie = create_movie()
movie.write_videofile('VideoCompilation\VideoFiles\\videos\movie.mp4', threads = 8, preset='ultrafast', logger=None, fps=30)
