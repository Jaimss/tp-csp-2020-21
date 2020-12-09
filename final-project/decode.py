import cv2
import os
from util import decode
import numpy as np

message = []

print('[DECODER] Decoding Message...')

# loop through all videos
videos = os.listdir('./message_output')
for video_title in sorted(videos):
    bin_str = ''
    capture = cv2.VideoCapture(os.path.join('./message_output', video_title))

    while capture.isOpened():
        _, frame = capture.read()
        if frame is None:
            break

        # display the image
        cv2.imshow('frame', frame)

        # get the rgb (bgr) color from the frame
        b = np.mean(frame[:, :, :1])
        g = np.mean(frame[:, :, 1:2])
        r = np.mean(frame[:, :, 2:])

        # check if red/blue
        if b > g and b > r:
            bin_str += '1'
        else:
            bin_str += '0'

    # add the binary to the message
    message.append(int(bin_str))

    # release video
    capture.release()
    cv2.destroyAllWindows()
    print(f'[DECODER] Video {video_title} complete.')

# send the decoded message
decoded = decode(message)
print('[DECODER] All Done! Your message is:')
print(decoded)
