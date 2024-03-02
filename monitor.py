import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import phub
import os
import re

def phub_download(url):
    quality = os.getenv('QUALITY')
    client = phub.Client()
    video = client.get(url)
    print("Downloading: " + video.title + " Quality: " + quality)
    filename = '/tmp/downloads/' + sanitize_filename(video.title) + video.id + '.mp4'
    if check_file_exists(filename):
        print(f"The file '{filename}' exists. Skipping")
    else:
        print(f"The file '{filename}' does not exist. Proceeding")
        video.download(filename, quality)



def sanitize_filename(filename):
    # Remove invalid characters
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    return filename


def check_file_exists(filename):
    return os.path.isfile(filename)


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('/tmp/download.txt'):
            with open(event.src_path, 'r+') as f:  # open file in read / write mode
                lines = f.readlines()
                f.seek(0)  # move file cursor to beginning
                for line in lines:
                    try:
                        print("Processing:" + line.strip())
                        phub_download(line.strip())
                    except subprocess.CalledProcessError:
                        # If command fails, write line back to file
                        f.write(line)
                # f.truncate()  # remove remaining lines

class InitialProcessing():
    def process(self, path):
        with open(path, 'r+') as f:  # open file in read / write mode
            lines = f.readlines()
            f.seek(0)  # move file cursor to beginning
            for line in lines:
                try:
                    print("Processing:" + line.strip())
                    phub_download(line.strip())
                except subprocess.CalledProcessError:
                    # If command fails, write line back to file
                    f.write(line)


if __name__ == '__main__':
    InitialProcessing().process('/tmp/download.txt')
    observer = Observer()
    event_handler = FileHandler()
    observer.schedule(event_handler, path='/tmp/download.txt', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
