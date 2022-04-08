from deepgram import Deepgram
import asyncio, json
import requests
import paralleldots as pd
import runpy
from pathlib import Path
import emoji
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, Radiobutton
from tkinter import StringVar, IntVar
from tkinter import filedialog
import threading

import os
import subprocess
import requests
global credit_text

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

global canvas

global mimeType

# tkdesigner -o D:/ToneFinderNew https://www.figma.com/file/XQWQf4cVtDRuHA6Krgwzvq/MainMenu-(Copy)?node-id=0%3A1 351991-109ed3fe-19a4-4228-9ac1-52cb7d97a870
# 53e7af871eea59ba966960632dcb550fff77d2ab
DEEPGRAM_API_KEY = '53e7af871eea59ba966960632dcb550fff77d2ab'

def please():
    print("haha!")
'''GUI (Graphical User Interface) starts from here!!'''

window = Tk()

window.geometry("1440x1024")
window.state('zoomed')
window.configure(bg = "#36DEE5")
window.iconbitmap(relative_to_assets("tonefinder_icon_Dow_icon.ico"))
window.title("ToneFinder")

global button_1
global button_2


global Title, Slogan, footerText

global menuTitle, menuSlogan


mimeType = StringVar()  # is a string variable but in the original code mimeType was being set an object.
mimeType.set('Initialize')  # So the later print statement will print something

MIMETYPE = mimeType.get()


def display_current_mimetype():
    print(mimeType.get())


# When Recorded Audio is clicked

def openRecordedAudio():

    window.title("ToneFinder - Recorded Audio")

    button_2.place_forget()
    button_1.place_forget()
    button_4.place(
        x=956.0,
        y=524.0,
        width=284.0,
        height=107.0
    )
    button_3.place(
        x=254.0,
        y=524.0,
        width=284.0,
        height=107.0
    )

    canvas.itemconfigure(Title, state='hidden')
    canvas.itemconfigure(Slogan, state='hidden')
    canvas.itemconfigure(MenuTitle, state='normal')
    canvas.itemconfigure(MenuSlogan, state='normal')

    MP2.place(x=170, y=350)
    MP3.place(x=430, y=350)
    MP4.place(x=680, y=350)
    WAV.place(x=930, y=350)
    FLAC.place(x=1180, y=350)

    global ResultTitle




global ProcessTitle
global button_8

global RProcessSubtitle
global button_9
global filename

def backToUpload():
    button_4.place(
        x=956.0,
        y=524.0,
        width=284.0,
        height=107.0
    )
    button_3.place(
        x=254.0,
        y=524.0,
        width=284.0,
        height=107.0
    )



    canvas.itemconfigure(Title, state='hidden')
    canvas.itemconfigure(Slogan, state='hidden')
    canvas.itemconfigure(MenuTitle, state='normal')
    canvas.itemconfigure(MenuSlogan, state='normal')
    canvas.itemconfigure(RProcessSubtitle, state='hidden')



    MP2.place(x=170, y=350)
    MP3.place(x=430, y=350)
    MP4.place(x=680, y=350)
    WAV.place(x=930, y=350)
    FLAC.place(x=1180, y=350)


    button_8.place_forget()

    if(mimeType.get() == ''):
        print("No selected!")

def startProcessing():
    runProcessing()
    thread.start()


def openExplorer():

    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Audio Files", ".wav .mp3 .mp4 .flac .mp2"),
                                                     ("all files",
                                                      "*.*")))
    print(filename)

    canvas.itemconfigure(MenuTitle, state='hidden')
    canvas.itemconfigure(MenuSlogan, state='hidden')
    MP2.place_forget()
    MP3.place_forget()
    MP4.place_forget()
    WAV.place_forget()
    FLAC.place_forget()
    button_3.place_forget()
    button_4.place_forget()

    process_emoji = emoji.emojize(':victory_hand:')

    global button_8
    global button_10
    global RProcessTitle
    global RProcessSubtitle
    global button_10_image

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_10 = Button(
        image=button_10_image,
        borderwidth=0,
        highlightthickness=0,
        command=startProcessing,
        relief="flat"
    )
    button_10.place(
        x=580.0,
        y=532.0,
        width=350.0,
        height=111.0
    )

    button_8 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=backToUpload,
        relief="flat"
    )

    RProcessTitle = canvas.create_text(
        540.0,
        110.0,
        anchor="nw",
        text=f"Your file is ready to process!{process_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 40 * -1)
    )

    RProcessSubtitle = canvas.create_text(
        540.0,
        200.0,
        anchor="nw",
        text=filename,
        fill="#000000",
        font=("Agency FB", 20 * -1)
    )



    if(filename == ''):
        print("No file")

        RProcessSubtitle = canvas.create_text(
            340.0,
            200.0,
            anchor="nw",
            text="Looks like you didn't select a file. Please select an file to continue or... it will go wrong!",
            fill="#000000",
            font=("Agency FB", 30 * -1)
        )
        button_8.place(
            x=606.0,
            y=524.0,
            width=284.0,
            height=107.0
        )

        canvas.itemconfigure(RProcessTitle,state='hidden')
        canvas.itemconfigure(RProcessSubtitle, state='normal')
        button_10.place_forget()


####################################################################
global response
global ResultTitle

global Tone

################################# Deepgram #######################################
async def transcribe():
        # Initializes the Deepgram SDK
        global response

        dg_client = Deepgram(DEEPGRAM_API_KEY)

        global filename
        global PATH_TO_FILE
        PATH_TO_FILE = filename

        with open(filename, 'rb') as audio:
            source = {'buffer': audio, 'mimetype': MIMETYPE}
            options = {'punctuate': True, 'language': 'en-US'}

            print('Requesting transcript...')
            print('Your file may take up to a couple minutes to process.')
            print('While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s.')
            print('To learn more about customizing your transcripts check out developers.deepgram.com')

            response = await dg_client.transcription.prerecorded(source, options)
            print(response)
            print(response['results']['channels'][0]['alternatives'][0]['transcript'])
            mainText =  (response['results']['channels'][0]['alternatives'][0]['transcript'])

            pd.set_api_key('pz68hppUKbIUvVL4ByrRhAB1rF1fUgErwAYrxeuNOkQ')

            pd.get_api_key()
            emotion = pd.emotion(mainText)
            print(emotion)

            happy_emo = (emotion['emotion']['Happy'])
            angry_emo = (emotion['emotion']['Angry'])
            fear_emo = (emotion['emotion']['Fear'])
            bored_emo = (emotion['emotion']['Bored'])
            excited_emo = (emotion['emotion']['Excited'])
            sad_emo = (emotion['emotion']['Sad'])

            if (happy_emo > max(angry_emo,fear_emo,bored_emo,sad_emo,excited_emo)):

                happy()
            elif(angry_emo > max(happy_emo,sad_emo,fear_emo,excited_emo,bored_emo)):
                angry()
            elif (fear_emo > max(happy_emo, sad_emo,angry_emo, excited_emo, bored_emo)):
                fear()
            elif (bored_emo > max(happy_emo, sad_emo, angry_emo, excited_emo, fear_emo)):
                bored()
            elif (excited_emo > max(happy_emo, sad_emo, angry_emo, bored_emo, fear_emo)):
                 excited()
            elif (sad_emo > max(happy_emo, excited_emo, angry_emo, bored_emo, fear_emo)):
                sad()




################################### Result Showing Functions ########################
button_12_image = PhotoImage(file=relative_to_assets("button_0.png"))
button_14_image = PhotoImage(file=relative_to_assets("button_14.png"))
button_10_image = PhotoImage(file=relative_to_assets("button_10.png"))

def happy():
    global button_12, button_14
    global button_12_image
    global button_14_image
    global credit_text

    canvas.itemconfigure(ProcessTitle, state='hidden')
    canvas.itemconfigure(ProcessSubtitle, state='hidden')
    canvas.itemconfigure(credit_text, state='hidden')
    canvas.itemconfigure(footerText,state='normal')
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()

    happy_emoji = emoji.emojize(':smiling_face:')
    resultText = canvas.create_text(
        685.0,
        210.0,
        anchor="nw",
        text=f"HAPPY {happy_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 48 * -1)
    )

    button_12 = Button(
        image=button_12_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )

    button_14 = Button(
        image=button_14_image,
        borderwidth=0,
        highlightthickness=0,
        command=quit,
        relief="flat"
    )

    button_12.place(
        x=277.0,
        y=410.0

    )
    button_14.place(
        x=902.0,
        y=410.0,
        width=350.0,
        height=111.0
    )

    ResultTitle = canvas.create_text(
        615.0,
        120.0,
        anchor="nw",
        text="We Detected it's Tone! ",
        fill="#000000",
        font=("Barlow Condensed Regular", 38 * -1)
    )


def sad():
    canvas.itemconfigure(ProcessTitle, state='hidden')
    canvas.itemconfigure(ProcessSubtitle, state='hidden')
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()

    global button_12, button_14
    global button_12_image
    global button_14_image

    button_12 = Button(
        image=button_12_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )

    button_14 = Button(
        image=button_14_image,
        borderwidth=0,
        highlightthickness=0,
        command=quit,
        relief="flat"
    )

    button_12.place(
        x=277.0,
        y=410.0

    )
    button_14.place(
        x=902.0,
        y=410.0,
        width=350.0,
        height=111.0
    )

    global resultText
    sad_emoji = emoji.emojize(':crying_face:')

    resultText = canvas.create_text(
        685.0,
        210.0,
        anchor="nw",
        text=f"SAD {sad_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 48 * -1)
    )

    ResultTitle = canvas.create_text(
        615.0,
        120.0,
        anchor="nw",
        text="We Detected it's Tone! ",
        fill="#000000",
        font=("Barlow Condensed Regular", 38 * -1)
    )


def excited():
    canvas.itemconfigure(ProcessTitle, state='hidden')
    canvas.itemconfigure(ProcessSubtitle, state='hidden')
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()

    global button_12, button_14
    global button_12_image
    global button_14_image

    button_12 = Button(
        image=button_12_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )

    button_14 = Button(
        image=button_14_image,
        borderwidth=0,
        highlightthickness=0,
        command=quit,
        relief="flat"
    )

    button_12.place(
        x=277.0,
        y=410.0

    )
    button_14.place(
        x=902.0,
        y=410.0,
        width=350.0,
        height=111.0
    )

    global resultText
    excited_emoji = emoji.emojize(':star-struck:')

    resultText = canvas.create_text(
        655.0,
        210.0,
        anchor="nw",
        text=f"EXCITED {excited_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 48 * -1)
    )

    ResultTitle = canvas.create_text(
        615.0,
        120.0,
        anchor="nw",
        text="We Detected it's Tone! ",
        fill="#000000",
        font=("Barlow Condensed Regular", 38 * -1)
    )


def bored():
    canvas.itemconfigure(ProcessTitle, state='hidden')
    canvas.itemconfigure(ProcessSubtitle, state='hidden')
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()

    global button_12, button_14
    global button_12_image
    global button_14_image

    button_12 = Button(
        image=button_12_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )

    button_14 = Button(
        image=button_14_image,
        borderwidth=0,
        highlightthickness=0,
        command=quit,
        relief="flat"
    )

    button_12.place(
        x=277.0,
        y=410.0

    )
    button_14.place(
        x=902.0,
        y=410.0,
        width=350.0,
        height=111.0
    )

    global resultText

    bored_emoji = emoji.emojize(':yawning_face:')

    resultText = canvas.create_text(
        665.0,
        210.0,
        anchor="nw",
        text=f"BORED {bored_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 48 * -1)
    )

    ResultTitle = canvas.create_text(
        615.0,
        120.0,
        anchor="nw",
        text="We Detected it's Tone! ",
        fill="#000000",
        font=("Barlow Condensed Regular", 38 * -1)
    )

def fear():
    canvas.itemconfigure(ProcessTitle, state='hidden')
    canvas.itemconfigure(ProcessSubtitle, state='hidden')
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()

    global button_12, button_14
    global button_12_image
    global button_14_image

    button_12 = Button(
        image=button_12_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )

    button_14 = Button(
        image=button_14_image,
        borderwidth=0,
        highlightthickness=0,
        command=quit,
        relief="flat"
    )

    button_12.place(
        x=277.0,
        y=410.0

    )
    button_14.place(
        x=902.0,
        y=410.0,
        width=350.0,
        height=111.0
    )

    global resultText
    fear_emoji = emoji.emojize(':face_screaming_in_fear:')

    resultText = canvas.create_text(
        665.0,
        210.0,
        anchor="nw",
        text=f"FEAR {fear_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 48 * -1)
    )

    ResultTitle = canvas.create_text(
        615.0,
        120.0,
        anchor="nw",
        text="We Detected it's Tone! ",
        fill="#000000",
        font=("Barlow Condensed Regular", 38 * -1)
    )


def angry():
    canvas.itemconfigure(ProcessTitle, state='hidden')
    canvas.itemconfigure(ProcessSubtitle, state='hidden')
    button_5.place_forget()
    button_6.place_forget()
    button_7.place_forget()

    global button_12, button_14
    global button_12_image
    global button_14_image

    button_12 = Button(
        image=button_12_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )

    button_14 = Button(
        image=button_14_image,
        borderwidth=0,
        highlightthickness=0,
        command=quit,
        relief="flat"
    )

    button_12.place(
        x=277.0,
        y=410.0

    )
    button_14.place(
        x=902.0,
        y=410.0,
        width=350.0,
        height=111.0
    )


    global resultText
    angry_emoji = emoji.emojize(':angry_face:')

    resultText = canvas.create_text(
        665.0,
        210.0,
        anchor="nw",
        text=f"ANGRY {angry_emoji}",
        fill="#000000",
        font=("Barlow Condensed Regular", 48 * -1)
    )

    ResultTitle = canvas.create_text(
        615.0,
        120.0,
        anchor="nw",
        text="We Detected it's Tone! ",
        fill="#000000",
        font=("Barlow Condensed Regular", 38 * -1)
    )


######################################################################

def showResult():
    global ResultTitle


def runProcessing():
    openProcessingMenu()

def runTranscribe():
    asyncio.run(transcribe())



thread = threading.Thread(
    target = runTranscribe

)



def openProcessingMenu():
    global button_8
    global button_10
    global RProcessTitle
    canvas.itemconfigure(RProcessSubtitle,state='hidden')
    canvas.itemconfigure(RProcessTitle,state='hidden')
    button_8.place_forget()
    button_10.place_forget()

    canvas.itemconfigure(RProcessSubtitle,state='hidden')
    button_5.place(
        x=200.0,
        y=524.0,
        width=284.0,
        height=107.0
    )

    button_6.place(
        x=1047.0,
        y=524.0,
        width=284.0,
        height=107.0
    )

    button_7.place(
        x=627.0,
        y=524.0,
        width=284.0,
        height=107.0
    )

    canvas.itemconfigure(ProcessTitle, state='normal')
    canvas.itemconfigure(ProcessSubtitle, state='normal')
    canvas.itemconfigure(credit_text, state='normal')

    canvas.itemconfigure(footerText, state='hidden')





canvas = Canvas(
    window,
    bg = "#36DEE5",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)

################################## Record Audio Menu Starts #################################


################################## Recoding Audio Menu #######################################



MenuTitle = canvas.create_text(
    315.0,
    110.0,
    anchor="nw",
    text="Find the Tone of Any Recorded Audio with Tone Finder!",
    fill="#000000",
    font=("Barlow Condensed Regular", 48 * -1)
)

MenuSlogan = canvas.create_text(
    559.0,
    215.0,
    anchor="nw",
    text="We accept various types of Audio Formats, including mp4s!",
    fill="#000000",
    font=("Barlow Condensed", 20 * -1)
)

MP3 = Radiobutton(window, text="MP3 Format", variable=mimeType,
            height=5,
            width=20, value='audio/mp3', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype,relief="solid",font =("Agency FB", 14))

MP4 = Radiobutton(window, text="MP4 Format", variable=mimeType,
            height=5,
            width=20, value='audio/mp4', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype,relief="solid",font =("Agency FB", 14))
MP2 = Radiobutton(window, text="MP2 Format", variable=mimeType,
            height=5,
            width=20, value='audio/mp2', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype,relief="solid",font =("Agency FB", 14))
WAV = Radiobutton(window, text="WAV Format", variable=mimeType,
            height=5,
            width=20, value="audio/wav", bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype,relief="solid",font =("Agency FB", 14))
FLAC = Radiobutton(window, text="FLAC Format", variable=mimeType,
            height=5,
            width=20, value='audio/flac', bg="#36DEE5",
            activebackground="#36DEE5", command=display_current_mimetype,relief="solid",font =("Agency FB", 14))


def runSnakeGame():
    subprocess.Popen(relative_to_assets("snakegame.exe"))



def runTicTacToe():
    subprocess.Popen(relative_to_assets("tictac.exe"))

def runDotBoxes():
    subprocess.Popen(relative_to_assets("dots_boxes.exe"))


def runRecorder():
    subprocess.Popen(relative_to_assets("Record.exe"))

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=runRecorder,
    relief="flat"
)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=openExplorer,
    relief="flat"
)


canvas.itemconfigure(MenuTitle,state='hidden')
canvas.itemconfigure(MenuSlogan,state='hidden')

button_3.place_forget()
button_4.place_forget()
################################## Recoding Audio Menu End #######################################



################################## Main Menu #######################################
Title = canvas.create_text(
    623.0,
    110.0,
    anchor="nw",
    text="ToneFinder",
    fill="#000000",
    font=("Agency FB", 70 * -1)
)

Slogan = canvas.create_text(
    459.0,
    215.0,
    anchor="nw",
    text="Find the Tone of any audio, fast and secure!",
    fill="#000000",
    font=("Barlow Condensed", 40 * -1)
)

heart_emoji = emoji.emojize(':blue_heart:')

footerText = canvas.create_text(
    589.0,
    691.0,
    anchor="nw",
    text=f"Built with {heart_emoji} and Deepgram by @MrBudDesigner ",
    fill="#000000",
    font=("Barlow Condensed Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=openRecordedAudio,
    relief="flat"
)
button_1.place(
    x=258.0,
    y=469.0,
    width=335.0,
    height=154.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command='',
    relief="flat"
)
button_2.place(
    x=913.0,
    y=469.0,
    width=335.0,
    height=154.0
)


################################## Main Menu End #######################################




################################# Processing Menu Start ##################################

ProcessTitle = canvas.create_text(
    380.0,
    110.0,
    anchor="nw",
    text="Your File is being Processed! It may take a couple of minutes. ",
    fill="#000000",
    font=("Barlow Condensed Regular", 38 * -1)
)

ProcessSubtitle = canvas.create_text(
    480.0,
    190.0,
    anchor="nw",
    text="I know, waiting is boring. Want to play a simple game?",
    fill="#000000",
    font=("Barlow Condensed Regular", 30 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=runSnakeGame,
    relief="flat"
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=runTicTacToe,
    relief="flat"
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=runDotBoxes,
    relief="flat"
)

credit_text = canvas.create_text(
    659.0,
    691.0,
    anchor="nw",
    text=f"Games built by Aqeel Anwar",
    fill="#000000",
    font=("Barlow Condensed Regular", 20 * -1)
)

canvas.itemconfigure(ProcessTitle,state='hidden')
canvas.itemconfigure(ProcessSubtitle,state='hidden')
canvas.itemconfigure(credit_text,state='hidden')




def quit():
    window.destroy()

window.resizable(False, False)
window.mainloop()

'''Logic part'''

#  print(response['results']['channels'][0]['alternatives'][0]['transcript'])

