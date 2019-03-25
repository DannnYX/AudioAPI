import time
import random
import cfg
import threading
import keyboard
import pyaudio
from pygame import mixer
from pygame import sndarray
from audio_api import AudioBOX
from audio_api import morse_encode
from notes_data import ocatave_1

cfg.init()


def kbd_callback(e):
    for key_code in list(keyboard._pressed_events):
        if key_code in ocatave_1:
            play_piano(ocatave_1.get(key_code))


def play_piano(note):
    stream = p.open(format=pyaudio.paInt32, channels=1, rate=44100, output=True)
    bit_stream = AudioBOX.gen_note_stream(note, duration=3)
    snd = sndarray.make_sound(bit_stream)
    snd.play()


def group(n, items):
    ns = [iter(items)] * n
    while True:
        yield [next(a) for a in ns]


mixer.pre_init(44100, size=16, channels=1)
mixer.init()
print('eee')
p = pyaudio.PyAudio()
keyboard.hook(kbd_callback)
keyboard.wait()
