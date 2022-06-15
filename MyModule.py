import time
import random
from winotify import Notification, audio

class MyModule():

    def hello_world():
        print("Hello, World!")

    def advancedprint(string, amount):
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

    def __init__(self):
        super(MyModule, self).__init__()