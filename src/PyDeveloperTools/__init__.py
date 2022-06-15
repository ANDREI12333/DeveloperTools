import time
import random
from winotify import Notification, audio
from tkinter import messagebox
pydtversion = "1.4.0"

class DeveloperTools():

    def hello_world():
        print("Hello, World!")

    def advancedprint(string="Hello, World!", amount=1):
        count = 0
        while (count < amount):
            count = count + 1
            print(string)

    def random(amount, amount2):
         print(random.randint(amount, amount2))

    def Notify(title="Hello there!", description="Hello, World!", appname="Python", sound=audio.Default, AudioLoop=False):
        toast = Notification(app_id=appname, title=title, msg=description, duration="short")
        toast.set_audio(sound, loop=AudioLoop)
        toast.show()

    def wait(seconds=1, message="null"):
        time.sleep(seconds)
        if message != "null":
            print(message)

    def alert(title="Alert", description="Hello, World!", appname="Python"):
        toast = Notification(app_id=appname, title=title, msg=description, duration="short")
        toast.set_audio(audio.LoopingAlarm, loop=True)
        toast.show()

    def spam(message="Hello, World!"):
        count = 0
        while (count < 50):
            count = count + 1
            print(message)

    def msgbox(information="Hello, World!", type="info", title="Hello, World!"):
        if type == "info":
            messagebox.showinfo(title, information)
        if type == "warn":
            messagebox.showwarning(title, information)
        if type == "error":
            messagebox.showerror(title, information)
        if type == "askquestion":
            messagebox.askquestion(title, information)
        if type == "askokcancel":
            messagebox.askokcancel(title, information)
        if type == "askyesno":
            messagebox.askyesno(title, information)
        if type == "askretrycancel":
            messagebox.askretrycancel(title, information)

    def about():
        print(f"PyDeveloperTools {pydtversion}")
        print("Thank you for using PyDeveloperTools!")

    def __init__(self):
        super(DeveloperTools, self).__init__()
