
import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
import emoji


def threading_rec(x):
    if x == 1:
        # If recording is selected, then the thread is activated
        t1 = threading.Thread(target=record_audio)
        t1.start()
        open2()
    elif x == 2:

        global open

        global recording
        recording = False

        open()

    elif x == 3:

        if file_exists:
            # Read the recording if it exists and play it
            data, fs = sf.read("recording.wav", dtype='float32')
            sd.play(data, fs)
            sd.wait()
    #  else:

    #  messagebox.showerror(title='ToneFinder - Audio Recorder',message="Record something to play")


# Fit data into queue
def callback(indata, frames, time, status):
    q.put(indata.copy())


# Recording function
def record_audio():
    global open2

    global recording
    recording = True
    global file_exists

    with sf.SoundFile("recording.wav", mode='w', samplerate=44100,
                      channels=2) as file:
        # Create an input stream to record audio without a preset time
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while recording == True:
                # Set the variable to True to allow playing the audio later
                file_exists = True
                # write into file
                file.write(q.get())


# Define the user interface for Voice Recorder using Python
win = Tk()
win.geometry("360x200")
win.title("ToneFInder - Audio Recorder")
win.config(bg="#36DEE5")


def open():
    magic_emoji = emoji.emojize(':sparkles:')
    top = Toplevel(win)
    top.title("ToneFinder - Recording Finished")
    top.geometry("350x180")
    top.config(bg="#36DEE5")
    top.iconbitmap('C:\\Users\\nethm\\Downloads\\My App Icon.ico')

    Label(top, text="Recording Finished!", font=("Agency FB", 14), bg="#36DEE5").place(x=110, y=10)
    Label(top, text=f"Take a look at the ToneFinder folder{magic_emoji}", font=("Agency FB", 14),
          bg="#36DEE5").place(x=70, y=40)

    top.resizable(False, False)
    top.mainloop()


def open2():
    mic_emoji = emoji.emojize(':microphone:')
    top1 = Toplevel(win)
    top1.title("ToneFinder - Recording Started")
    top1.geometry("350x180")
    top1.config(bg="#36DEE5")
    top1.iconbitmap('C:\\Users\\nethm\\Downloads\\My App Icon.ico')

    Label(top1, text="Recording Started", font=("Agency FB", 14), bg="#36DEE5").place(x=110, y=10)
    Label(top1, text=f"Speak to the mic loudly as you can!{mic_emoji}", font=("Agency FB", 14),
          bg="#36DEE5").place(
        x=70, y=40)

    top1.resizable(False, False)
    top1.mainloop()


q = queue.Queue()
# Declare variables and initialise them
recording = False
file_exists = False

tone_emoji = emoji.emojize(':musical_note:')

# Label to display app title in Python Voice Recorder Project
title_lbl = Label(win, text=f"Record Audio with ToneFinder{tone_emoji}", font=("Agency FB", 16),
                  bg="#36DEE5").place(x=90, y=20)

# Button to record audio
record_btn = Button(win, text="Record Audio", command=lambda m=1: threading_rec(m), font=("Agency FB", 14))
# Stop button
stop_btn = Button(win, text="Stop Recording", command=lambda m=2: threading_rec(m), font=("Agency FB", 14))
# Play button
# play_btn = Button(win, text="Play Recording", command=lambda m=3: threading_rec(m),font =("Agency FB", 14))
# Position buttons
record_btn.place(x=50, y=90)
stop_btn.place(x=205, y=90)
# play_btn.place(x = 240, y=90)
win.resizable(False, False)
win.mainloop()



