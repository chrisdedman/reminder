from sys import exit
from AppKit import NSSound
import time
import os

list = []
# Here's your daily date append in the file: history_reminder.txt
def todaysDate():
    daily_clock = time.localtime()
    daily_date = time.strftime("%a, %b %d %Y", daily_clock)
    data = "----------------\n" + daily_date + "\n----------------"
    with open("history_reminder.txt", 'a') as output:
        output.write("\n" + data + '\n')
        output.close()
        return Alarm()

def Alarm():
    global list
    end_time1 = input("At what time do you want an alarm?\n(Format 24h: hh:mm:ss)\n>>")
    reminder = input("What's the reminder for?\n>>")
    all = "Time: " + end_time1 + " Your Reminder is: " + reminder
    list.append(all)
    Last_reminder = input("Do you want to see your all reminder schedules?\n[yes/no]\n>>")
    if 'yes' in Last_reminder:
        print(list)
        question = input("Are you done?")
        if 'yes' in question:
            pass
    else:
        pass

    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        clock = time.localtime()  # get struct_time
        Timer = time.strftime("%a, %b %d %Y%, %X%p (%Z)", clock)
        # ------------------------- #
        # ------ Timer Loop ------- #
        # ------------------------- #
        if end_time1 in Timer:
            its_time = True
            print("Your Reminder is:\n(",reminder,")")
            # ----------------------------- #
            # ------ Prepare Sounds ------- #
            # ----------------------------- #
            sound = NSSound.alloc()
            sound.initWithContentsOfFile_byReference_(
                'reminder_voice.mp3', True)        # < ------------------------- Here should be your song.
            sound.play()
            # ----------------------------------------------------------------------------------------- #
            # ------ Add 5 seconds time sleep (time the song play) before to close the program ------- #
            # ----------------------------------------------------------------------------------------- #
            time.sleep(8)
            while sound.isPlaying():
                another = input("Do you want an other one?\n[yes/no]\n>>")
                if another == 'yes':
                    return Alarm()
                else:
                    # Here you print the history of your day, and append it to the history file: history_reminder.txt 
                    print(list)
                    with open("history_reminder.txt", 'a') as output:
                        for row in list:
                            output.write(str(row) + '\n')
                    break
            # --------------------------------------------- #
            # ------ Print this until the time out! ------- #
            # --------------------------------------------- #
        else:
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time1)
            print("\tYour reminder is:", reminder)
            print("." * 50)
            time.sleep(1)
            os.system('clear')
            its_time = False

if __name__ == "__main__":
    todaysDate()
