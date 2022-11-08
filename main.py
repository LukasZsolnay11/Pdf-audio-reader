from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def extract_text():
    file = filedialog.askopenfile(parent=root, mode="rb", title="Choose a PDF File")
    if file != None:
        pdfReader = PyPDF2.PdfFileReader(file)
        global text_extracted
        text_extracted = ""
        for pageNum in range(pdfReader.numPages):
            pageObject = pdfReader.getPage(pageNum)
            text_extracted += pageObject.extractText()
        file.close()

def speak_text():
    global rate
    global male
    global female
    rate = int(rate.get())
    engine.setProperty('rate', rate)
    male = int(male.get())
    female = int(female.get())
    all_voices = engine.getProperty('voices')
    maleVoice = all_voices[0].id
    femaleVoice = all_voices[1].id

    if(male == 0 and female == 0) or (male == 1 and female == 1):
        engine.setProperty('voice', maleVoice)
    elif male == 0 and female == 1:
        engine.setProperty('voice', femaleVoice)
    else:
        engine.setProperty('voice', maleVoice)

    engine.say(text_extracted)
    engine.runAndWait()


def stop_speaking():
    engine.stop()


def application(root):
    root.geometry('{}x{}'.format(700, 600))
    root.resizable(width=False, height=False)
    root.title("PDF to Audio")
    root.configure(bg="#BF5B5B")
    global rate, male, female

    frame1 = Frame(root, width=500, height=200)
    frame2 = Frame(root, width=500, height=450, bg="#BF5B5B")
    frame1.pack(side="top", fill="both")
    frame2.pack(side="top", fill="y")

    #frame1 Widgets
    name1 = Label(frame1, text="PDF to Audio", fg="black", font="Cabin 30")
    name1.pack()

    name2 = Label(frame1, text="Hear Your PDF", fg="black", font="Orbitron 30")
    name2.pack()

    #frame2 Widgets

    btn = Button(frame2, text="Select PDF File", activeforeground="red", command=extract_text,
                 padx="70", pady="10", fg="white", bg="#A31621", font="Sora")

    btn.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text="Rate of Speech (0 - 150)", fg="black", font="Roboto")
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)
    rate = Entry(frame2,  fg="black", bg="white", font="Ariel")
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(frame2, text="Select Voice:", fg="black", font="Roboto")
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)
    male = IntVar()

    male_opt = Checkbutton(frame2, text="Male", bg="#BFDBF7", variable=male, onvalue=1, offvalue=0)
    male_opt.grid(row=2, column=1, pady=0, padx=30, sticky=W)

    female = IntVar()
    female_opt = Checkbutton(frame2, text="Female", bg="pink", variable=female, onvalue=1, offvalue=0)
    female_opt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submit_btn = Button(frame2, text="Play PDF File", command=speak_text, bg="#0FDD0F",
                        activeforeground="red", padx="60", pady="10", font="Rubik")
    submit_btn.grid(row=4, column=0, pady=65)

    stop_btn = Button(frame2, text="Stop Playing", command=stop_speaking, bg="#E60707",
                     activeforeground="red", padx="60", pady="10", font="Rubik")

    stop_btn.grid(row=4, column=1, pady=65)


if __name__ == "__main__":
    mytext, rate, male, female = "", 100, 0, 0
    engine = pyttsx3.init()
    root = Tk()
    application(root)
    root.mainloop()










