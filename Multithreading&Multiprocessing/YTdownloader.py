
# from pytube import YouTube

# youtube_video_url = 'https://www.youtube.com/watch?v=668nUCeBHyY'

# try:
#     yt_obj = YouTube(youtube_video_url)

#     filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

#     # download the highest quality video
#     filters.get_highest_resolution().download()
#     print('Video Downloaded Successfully')
# except Exception as e:
#     print(e)

from pyyoutube import Api
from pytube import YouTube
from threading import Thread


def threading():
    # Call download_videos function
    t1 = Thread(target=download_videos)
    t1.start()


def download_videos():
    # Create API Object
    api = Api(api_key='Enter API Key')

    if "youtube" in playlistId:
        playlist_id = playlistId[len(
            "https://www.youtube.com/playlist?list="):]
    else:
        playlist_id = playlistId

    print(playlist_id)
    # Get list of video links
    playlist_item_by_id = api.get_playlist_items(
        playlist_id=playlist_id, count=None, return_json=True)

    # Iterate through all video links
    for index, videoid in enumerate(playlist_item_by_id['items']):

        print(index, '-----', videoid)

        link = f"https://www.youtube.com/watch?v={videoid['contentDetails']['videoId']}"

        yt_obj = YouTube(link)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        # download the highest quality video
        filters.get_highest_resolution().download()

        print(f"Downloaded:- {link}")

    print("Success, Video Successfully downloaded")


if __name__ == "__main__":

    playlistId = 'https://www.youtube.com/playlist?list=PL-FbhHsDM2qH4JS70UuUxa4lVJZn4bsLD'

    threading()
