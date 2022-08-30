import os
import json
PATH_TO_VALID_CLIPS = 'VideoCompilation/ClipData/valid_clips.txt'
EMAIL = 'bungeeportfolio+submissions@gmail.com'

# reads clip valid clip names from file
def read_valid_clips_list():
    #read valid clips
    file = open(PATH_TO_VALID_CLIPS, 'r')
    valid_list = file.readlines()
    print(valid_list)
    return valid_list

# gets clip data
def get_clip_data(filename):
    file = open('VideoCompilation\ClipData\clips_data.json')
    clips_data = json.load(file)

    return clips_data[filename]

def write_results2file(streamer_data, video_title):
    os.remove('VideoCompilation/ClipData/desc.txt')
    with open('VideoCompilation/ClipData/desc.txt', 'w') as fp:

        TITLE = 'Daily VALORANT Twitch Clips | \"{}\"\n\n'.format(video_title)
        DESCRIPTION = '\"{}\"\n\nSend your clips to: {}\n\nStreamer Credits:\n'.format(video_title, EMAIL)

        fp.write(TITLE) 
        fp.write(DESCRIPTION)
        for count, streamer_name in enumerate(streamer_data):
            # write each item on a new line
            fp.write('{}: {}\n'.format(streamer_name, streamer_data[streamer_name]))

def get_streamer_links():
    clip_list = read_valid_clips_list()
    streamer_data = {}
    video_title = get_clip_data(clip_list[0].strip()).get('clipTitle')
    for clip_name in clip_list:
        clip_name = clip_name.strip()
        clip_data = get_clip_data(clip_name)

        streamer_link = clip_data.get('streamerLink')
        streamer_name = clip_data.get('streamerName')

        streamer_data.update( {streamer_name: streamer_link})

    return streamer_data, video_title

def create_video_data():
    streamer_data, video_title = get_streamer_links()
    write_results2file(streamer_data, video_title)


create_video_data()