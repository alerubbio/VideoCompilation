import os
import json

PATH_TO_MOVIE = 'VideoCompilation\VideoFiles\\videos\movie.mp4'
PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'

# reads clip valid clip names from file
def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    valid_list = file.readlines()
    return valid_list

# gets clip data
def get_clip_data(clipname):
    file = open('VideoCompilation\ClipData\clips_data.json')
    clips_data = json.load(file)

    return clips_data[clipname]

