from sys import exit
from AppKit import NSSound
import time
import os

def first_time_crate():
    end_time1 = input("At what time do you want an alarm?\n(Format: hh:mm:ss)\n>>")
    reminder = input("What's the reminder for?\n>>")
    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        named_tuple = time.localtime()  # get struct_time
        Timer = time.strftime("%a, %b %d %Y%, %X%p (%Z)", named_tuple)
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
                '/Users/chrisrollet/Desktop/Programming/Python Project/Clock Timer/Puppy Out1.m4a', True)
            sound.play()
            # ----------------------------------------------------------------------------------------- #
            # ------ Add 5 seconds time sleep (time the song play) before to close the program ------- #
            # ----------------------------------------------------------------------------------------- #
            time.sleep(10)
            while sound.isPlaying():
                another = input("Do you want an other one?\n[yes/no]\n>>")
                if another == 'yes':
                    return first_time_crate()
                else:
                    break
            # --------------------------------------------- #
            # ------ Print this until the time out! ------- #
            # --------------------------------------------- #
        else:
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time1)
            print("." * 50)
            time.sleep(1)
            os.system('clear')
            its_time = False

if __name__ == "__main__":
    first_time_crate()
