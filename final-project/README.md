# Final Project
Creating a Custom Encoder (2.3.1)

---

## Solution
I created an encoder/decoder in `util.py` where letters are modified by a random 'change amount', which is then sent as the first part of the encoded message. Those letters are
turned into integers and then their respective binary. The binary message is sent over, and the decoder does everything in reverse.

The graphical part:
- Users input the message via the command line.
- Video Files are created for each individual character.
- Everything runs at a certain frame rate so it can be properly decoded.
- The decoder opens the videos in order and plays them back watching for changes in color and recording the appropriate binary.
- The final message is displayed on screen.

---

#### Problems
- 1 & 2
    - Run encode & decode to get a gif file. When you decode it the message is `changeme` as well as a lot of binary.
    - Encoder writes squares to the screen, decoder then turns them back into binary.
- 3 & 4
    - Comments have been added to the code under the `example` directory.
- 5
    - a. You would change the `message` variable to something else or maybe user input
    - b. change the `drawer.shape` line
    - c. change the `ImageGrab.....save()` line to use a different name than `output.gif`
    - d. change the `drawer.color` line to use red not blue
    - e. change the line where you check `if g < 254` to check for red instead of blue
    - f. change to `drawer.goto` line to go to a different location
- 6
    - N/a
- 7,8,9,10 & 11
    - Ideas
        - use audio
        - use video
        - use images
    - Pick an idea
        - im gonna use video to make it work
        - binary will be displayed using colors
        - the decoder will watch the videos and "read" the colors
- 12, 13, 14
    - there will be encoding/decoding algorithms
    - algorithms for converting letters to binary/integers
    - binary will be sent using video form and read
    - everything above is feasable
- 17,18,19,20,21
    - met all of my goals and requirements for the encoder/decoder
    - tested all things multiple times like user input or different errors that occured and fixed them
- all remaining quesitons
    - will be answered in the video/code

---

### To Run the Program
In the root project directory execute
- `pip3 install -r requirements.txt`
  - Note: `pip3 -V` is `20.0.2`
  - Note: `python3 -V` is `Python 3.8.5`
Again in the root project directory execute
- `python3 encode.py`
- Follow the prompts on screen to encode a message.
- `python3 decode.py`
- Will decode the message.
Additional Requirements:
- `python3-tk`

---

### Goals
- Apply all you have learned to create or modify a custom encoding tool (not a traditional encryption algorithm) to encode a message.
- Explain how a code segment or program functions.
- Identify data storage and usage in your program.
- Explain how an abstraction manages complexity in your program.
- Describe a procedure call in your program.

### Materials
- Screen capturing (screenshot) software
- Screen recording (video) software

### Resources
- [Pair Programming](https://s3.amazonaws.com/lms-content.pltw.org/curriculum/HS/CS/General/PairProgramming.pdf)
- [2.3.1 Rubric](https://apcentral.collegeboard.org/pdf/ap-computer-science-principles-2021-create-performance-task-scoring-guidelines.pdf)
