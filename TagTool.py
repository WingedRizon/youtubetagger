from datetime import datetime
import pytchat
from pynput.keyboard import Controller


#Fetch Live Chat using Video ID
chat = pytchat.create(video_id="HGuF_CiV5D4")
#Create Controller object
keyboard = Controller()
#Fetch messages and simulate keypresses
start_time = datetime.now().strftime("%H:%M:%S").split(":")

while chat.is_alive():
    for c in chat.get().sync_items():
        msg = c.message

#Fetch the message
#Check if the message has the word !tag
#Add the timestamp + chapter name + user to a text fill

        message_cut = msg.split(" ")
        if message_cut[0].lower() == "!tag":
            with open('tags.txt', 'a', encoding="utf-8") as f:
                chapt_name = msg[5:]
                now_time = datetime.now().strftime("%H:%M:%S").split(":")
                timestamp = ""
                for x in range(3):
                    timestamp += str(int(now_time[x]) - int(start_time[x])) + ":"
                timestamp = timestamp[:-1]
                name = "%s - %s by %s" % (timestamp, chapt_name, c.author.name)
                f.write(name)
                f.write('\n')
                f.close()
                print(name)
        else:
            pass









def addMsg():
    pass

def countMsg():
    pass
