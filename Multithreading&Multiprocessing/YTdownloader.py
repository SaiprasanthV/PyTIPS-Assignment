
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


from pytube import YouTube
import logging
import threading
import time

file_size = 0


def complete_func(stream, file_handle):
    print('Video downloaded successfully !')


def show_progress_bar(chunk, file_handle, bytes_remaining):
    global file_size
    if file_size == 0:
        file_size = bytes_remaining
    else:
        r = float(file_size - bytes_remaining)
        print(str(round(r/float(file_size)*100, 0)) + '% of video downloaded')


def thread_function(url):
    logging.info("Thread %s: starting", url)
    yt = YouTube(url)
    print('Going to download:', yt.title)
    yt.register_on_progress_callback(show_progress_bar)
    yt.register_on_complete_callback(complete_func)
    yt.streams.filter(progressive=True).first().download()
    logging.info("Thread %s: finishing", url)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    YT_url_list = ['https://www.youtube.com/watch?v=qiwBjYhQ_-c&list=PL-FbhHsDM2qH4JS70UuUxa4lVJZn4bsLD&index=4',
                   'https://www.youtube.com/watch?v=movsj_dyrOQ&list=PL-FbhHsDM2qH4JS70UuUxa4lVJZn4bsLD&index=6']

    for url in YT_url_list:
        # print('url=  ', url)

        logging.info("Main    : before creating thread")
        x = threading.Thread(target=thread_function, args=(url,))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        # x.join()
        logging.info("Main    : all done")
