import os
from pathlib import Path
import cv2
from util import encode

# obtain user input for character shift amount and the message to send
message = input('[ENCODER] What is your message? ')
valid = False
while not valid:
    try:
        change_amount = int(input('[ENCODER] How many characters should each letter be shifted? '))
        valid = True
    except ValueError:
        pass

print('[ENCODER] Working...')

# encode the user's message
binary_data = encode(message, change_amount)

# make the output directory and clear any files
Path("./message_output").mkdir(parents=True, exist_ok=True)
os.system('rm -rf ./message_output/*')

for (i, binary_char) in enumerate(binary_data):
    # setup the video title
    # each character will be contained in one video file
    video_title = f'./message_output/{"{0:0=3d}".format(i)}.avi'

    # 1080p
    height = 168
    width = 300

    # make the video
    video = cv2.VideoWriter(video_title, cv2.VideoWriter_fourcc('M','J','P','G'), fps=30, frameSize=(width, height))

    # loop through the different binary digits in the character and
    # add their frames to the video.
    for binary_digit in str(binary_char):
        # 0 = red
        # 1 = blue
        if int(binary_digit) == 0:
            image = cv2.imread(os.path.join('./images', 'red.png'))
        else:
            image = cv2.imread(os.path.join('./images', 'blue.png'))
        video.write(image)

    # "release" the video and end the process
    cv2.destroyAllWindows()
    video.release()
    print(f'[ENCODER] Encoded {binary_char} into {video_title}.')

print('[ENCODER] Message successfully sent! Please send the \'message_output\' to someone with the decoding algorithm.')
