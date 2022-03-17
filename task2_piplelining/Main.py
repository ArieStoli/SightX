"""

Class Main:

DISCLAIMER: this code will probably not run.

This script defines a movie processing pipeline.
At an event of an addition of a new movie to a directory, the system shall:
    1. Copy it into a directory called 'Raw'
    2. Split the movie into frames and add them to the 'Train' directory
    3. Each frame will be converted to a compressed jpg format and saved in the 'Annotation' directory.
    
Using the watchdog module, the script initializes an Observer that'll monitor the target directory for inbound movies.

"""
import sys
import argparse
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Utils.Compressor import Compressor
from Utils.FrameSplitter import FrameSplitter

def pipeline(event):
    
    # Get the name of the movie so we can create the sub-directories in the Train and Annotation directories
    movie_name_w_suffix = event.src_path.split('\\')[-1]
    movie_name = movie_name.split('.')[:-1][0]
    
    # Copy the movie to the 'Raw' directory
    raw_path = os.path.join(raw_dir, movie_name)
    copy_file(event.src_path, raw_path)
    print(f'=== movie {movie_name} moved to {raw_dir} ===')
    
    # Create movie sub-directories
    os.mkdir(os.path.join(train_dir, movie_name))
    os.mkdir(os.path.join(annot_dir, movie_name))
    
    # Split the movie to frames using the FrameSplitter class.
    # Save frames under the movie sub-directory at the 'Train' directory
    train_path = os.path.join(train_dir, movie_name)
    splitter.split_movie(raw_path, movie_name, train_path)
    
    # Compress each frame that was created into .jpg using the Compressor class.
    # Save images in the movie sub-directory under 'Annotation'
    for frame in os.listdir(train_path):
        in_path = os.path.join(train_path, frame)
        compressor.compress_image(in_path, annot_dir, frame.split[0])
        
    print('Comperssion done')
        
    ### pipeline done. continue listening
        
# Used to copy the movie from target to raw
def copy_file(src, dst):
    shutil(src, dst)
    
# Init the directory observer
def build_observer(handler, path_to_watch):
    observer = Observer()
    observer.schedule(handler, path_to_watch, recursive=False)
    observer.start()
    return observer


#This section organizes the arguments of the command line into variables.
parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quality", required=True) #should be a integer between 1-100
args = parser.parse_args()
quality = args.quality

# Improvement: define a config.ini file and change paths there if need be.
raw_dir='./Raw'
train_dir='./Train'
annot_dir='./Annotation'

compressor = Compressor(quality)
splitter = FrameSplitter()
    
# turn on the directory event handler
event_handler_image_dir = FileSystemEventHandler()
event_handler_image_dir.on_created = pipeline
observer_image_dir = build_observer(event_handler_image_dir, './target')

# run as long the process is up. 
try:
    print("@@@@@@@@ script initialized @@@@@@@@")
    while True:
        time.sleep(1)
except Exception:
    print(str(Exception), 'process stopping...')
finally:
    observer_image_dir.stop()