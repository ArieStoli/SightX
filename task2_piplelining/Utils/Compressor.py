"""

Class Compressor

The Compressor object takes high quality frames and compresses them using OpenCV.
The quality parameter is defined in the command line whem running Main.py

"""

import cv2

class Compressor:

    def __init__(self, quality):
        self.__quality = quality
        
    def compress_image(self, in_path, out_dir, frame_name):
        img = cv2.imread(in_path)
        out_path = f'{out_dir}/{frame_name}.jpg'
        cv2.imwrite(out_path, img, [cv2.CV_IMWRITE_PNG_COMPRESSION, self.__quality])
