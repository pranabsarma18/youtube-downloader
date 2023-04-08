import pytube
from pytube import Playlist
import os

# Replace this with the URL of the YouTube playlist you want to download
playlist_url = 'https://www.youtube.com/playlist'

# Replace this with the path to the directory where you want to save the videos
download_dir = 'Playlist Videos'

# Create a playlist object
playlist = Playlist(playlist_url)

# Iterate through all the videos in the playlist
for video in playlist.videos:
    try:
        # Check if video already exists in the download directory
        video_dir = os.path.join(download_dir, video.title)
        if os.path.exists(video_dir):
            print(f'{video.title} already exists in {download_dir}. Skipping download.')
            continue
        
        print(f'Downloading {video.title}...')
        
        # Download the video
        video.streams.get_highest_resolution().download(output_path=download_dir)
        
    except pytube.exceptions.PytubeError:
        print(f'Error downloading {video.title}. Skipping video.')
        continue

print('All videos have been downloaded.')
