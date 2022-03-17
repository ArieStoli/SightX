"""

Class FrameSplitter

The FrameSplitter takes a movie and separetes the frames into individual images, using OpenCV.

"""

import cv2
import os

class FrameSplitter:

    def __init__(self):
        self.precentage_done = None # helps to keep track on splitting progress
        
    
    def split_movie(movie_path, movie_name, train_dir_path):
        # init variables
        self.precentage_done = []
        capture = cv2.VideoCapture(movie_path) # an array of frames
        total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'=== Split start. Splitting {total_frames} frames in movie {movie_name} ===')
        frame_number = 0
        
        # iterates over all frames, .read() pops the next frame and it is saved in a .png format
        while (True):
            success, frame = capture.read()
            if success:
                frame_img = f'frame_{frame_number}.png'
                cv2.imwrite(os.path.join(train_dir_path, frame_img), frame)
            else:
                break
            frame_number += 1
            
        capture.release()
        print(f'=== Split done on movie  ===')
        
    # Utility function that prints the progress for each 10th precentile
    def print_progress(frame_number, total_frames):
        precent = int(frame_number / total_frames * 100)
        if precent % 10 == 0 and precent not in self.precentage_done:
            self.precentage_done.append(precent)
            print(f'=== frame no. {frame_number}. {precent}% done. ===')