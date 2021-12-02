from adafruit_circuitplayground import cp
import time

morse_alphabet = [
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
]

increased = 0
prev_input = None

def start_new_message():
    # According to wikipedia,
    # the sequence for "new message" is
    # .-.-.
    cp.play_tone(300, 0.5);
    cp.play_tone(300, 1)
    cp.play_tone(300, 0.5);
    cp.play_tone(300, 1)
    cp.play_tone(300, 0.5);

def play_character(code):
    for x in code:
        if (x == '.'):
            cp.play_tone(300, 0.5)
        elif(x == '-'):
            cp.play_tone(300, 1)

def translate_int_to_morse(x):
    out = ""
    for i in str(x):
        for m in morse_alphabet:
            if m[0] == i:
                out += m[0]

    return out

def play_number_in_morse(x):
    for c in x:
        for m in morse_alphabet:
            if (c == m[0]):
                play_character(m[1])
        time.sleep(2)

def process_input(inp):
    global increased
    global prev_input
    global color

    if (prev_input == None):
        # First sample, do nothing
        pass
    elif inp > prev_input:
        increased = increased + 1


##############################
fp = open('input', 'r')
line = fp.readline()
while line:
    process_input(int(line))
    prev_input = int(line)
    line = fp.readline()

fp.close()

out = translate_int_to_morse(increased)

print(out)

while True:
    start_new_message()
    time.sleep(2)
    play_number_in_morse(out)
    time.sleep(5)
