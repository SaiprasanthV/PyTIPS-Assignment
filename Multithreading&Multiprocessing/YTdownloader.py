from pytube import YouTube
import logging
import threading
import time

file_size = 0


def complete_func(stream, file_handle):
    # function to indicate that the download is completed
    print('Video downloaded successfully !')


def show_progress_bar(chunk, file_handle, bytes_remaining):
    # function to show the progress of downloads
    global file_size
    if file_size == 0:
        file_size = bytes_remaining
    else:
        r = float(file_size - bytes_remaining)
        # calculates the download percentage
        print(str(round(r/float(file_size)*100, 0)) + '% of video downloaded')


def thread_function(url):
    # thread function to perform Multithreading
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
    # list of YuoTube URL links
    YT_url_list = ['https://www.youtube.com/watch?v=qiwBjYhQ_-c&list=PL-FbhHsDM2qH4JS70UuUxa4lVJZn4bsLD&index=4',
                   'https://www.youtube.com/watch?v=movsj_dyrOQ&list=PL-FbhHsDM2qH4JS70UuUxa4lVJZn4bsLD&index=6']

    for url in YT_url_list:
        logging.info("Main    : before creating thread")
        x = threading.Thread(target=thread_function, args=(url,))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        logging.info("Main    : all done")
