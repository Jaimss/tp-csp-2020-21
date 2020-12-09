# Final Project
Creating a Custom Encoder (2.3.1)

---

## Solution
I created an encoder/decoder in `util.py` where letters are modified by a random 'change amount', which is then sent as the first part of the encoded message. Those letters are
turned into integers and then their respective binary. The binary message is sent over, and the decoder does everything in reverse.

The graphical part:
- Users input the message via a GUI.
- The GUI creates an image with circles every x pixels.
- If the circles are BLUE its a 1, if they are RED its a 0.

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

---

#### Problems
- 1 & 2
    - Run encode & decode to get a gif file. When you decode it the message is `changeme` as well as a lot of binary.
