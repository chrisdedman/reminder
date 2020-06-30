from sys import exit
from AppKit import NSSound
import time

# ---------------------------------------------- #
# --- Variable Nap's Times / 24h Format --- #
# ---------------------------------------------- #
end_time1 = "Tue Jun 29 10:00:00 2020"
end_time2 = "Tue Jun 30 13:00:00 2020"
end_time3 = "Tue Jun 30 16:00:00 2020"
end_time4 = "Tue Jun 30 19:00:00 2020"

# ----------------------------- #
# ------ First Nap Time ------- #
# ----------------------------- #

def first_time_crate():
    global end_time1
    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        Timer = time.asctime(time.localtime(time.time()))
        # ------------------------- #
        # ------ Timer Loop ------- #
        # ------------------------- #
        if Timer == end_time1:
            its_time = True
            print("It's time to take your puppy out!")
        # ----------------------------- #
        # ------ Prepare Sounds ------- #
        # ----------------------------- #
            sound = NSSound.alloc()
            sound.initWithContentsOfFile_byReference_(
                '/Users/chrisrollet/Documents/Python Project/Clock Timer/Puppy Out1.m4a', True)
            sound.play()
        # ----------------------------------------------------------------------------------------- #
        # ------ Add 10 seconds time sleep (time the song play) before to close the program ------- #
        # ----------------------------------------------------------------------------------------- #
            time.sleep(10)
            while sound.isPlaying():
                second_time_crate()
        # --------------------------------------------- #
        # ------ Print this until the time out! ------- #
        # --------------------------------------------- #
        else:
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time1)
            print("." * 50)
            time.sleep(1)
            its_time = False

# ------------------------------ #
# ------ Second Nap Time ------- #
# ------------------------------ #

def second_time_crate():
    global end_time2
    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        Timer = time.asctime(time.localtime(time.time()))
        # ------------------------- #
        # ------ Timer Loop ------- #
        # ------------------------- #
        if Timer == end_time2:
            its_time = True
            print("It's time to take your puppy out!")
        # ----------------------------- #
        # ------ Prepare Sounds ------- #
        # ----------------------------- #
            sound = NSSound.alloc()
            sound.initWithContentsOfFile_byReference_(
                '/Users/chrisrollet/Documents/Python Project/Clock Timer/Puppy Out1.m4a', True)
            sound.play()
        # ----------------------------------------------------------------------------------------- #
        # ------ Add 10 seconds time sleep (time the song play) before to close the program ------- #
        # ----------------------------------------------------------------------------------------- #
            time.sleep(10)
            while sound.isPlaying():
                third_time_crate()
        # --------------------------------------------- #
        # ------ Print this until the time out! ------- #
        # --------------------------------------------- #
        else:
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time2)
            print("." * 50)
            time.sleep(1)
            its_time = False

# ----------------------------- #
# ------ Third Nap Time ------- #
# ----------------------------- #

def third_time_crate():
    global end_time3
    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        Timer = time.asctime(time.localtime(time.time()))
        # ------------------------- #
        # ------ Timer Loop ------- #
        # ------------------------- #
        if Timer == end_time3:
            its_time = True
            print("It's time to take your puppy out!")
        # ----------------------------- #
        # ------ Prepare Sounds ------- #
        # ----------------------------- #
            sound = NSSound.alloc()
            sound.initWithContentsOfFile_byReference_(
                '/Users/chrisrollet/Documents/Python Project/Clock Timer/Puppy Out1.m4a', True)
            sound.play()
        # ----------------------------------------------------------------------------------------- #
        # ------ Add 10 seconds time sleep (time the song play) before to close the program ------- #
        # ----------------------------------------------------------------------------------------- #
            time.sleep(10)
            while sound.isPlaying():
                forth_time_crate()
        # --------------------------------------------- #
        # ------ Print this until the time out! ------- #
        # --------------------------------------------- #
        else:
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time3)
            print("." * 50)
            time.sleep(1)
            its_time = False

# ---------------------------- #
# ------ Last Nap Time ------- #
# ---------------------------- #

def forth_time_crate():
    global end_time4
    its_time = False
    while its_time == False:
        its_time = False
        # ------------------------------------------ #
        # ------ Local Time in your country! ------- #
        # ------------------------------------------ #
        Timer = time.asctime(time.localtime(time.time()))
        # ------------------------- #
        # ------ Timer Loop ------- #
        # ------------------------- #
        if Timer == end_time4:
            its_time = True
            print("It's time to take your puppy out!")
        # ----------------------------- #
        # ------ Prepare Sounds ------- #
        # ----------------------------- #
            sound = NSSound.alloc()
            sound.initWithContentsOfFile_byReference_(
                '/Users/chrisrollet/Documents/Python Project/Clock Timer/Puppy Out1.m4a', True)
            sound.play()
        # ----------------------------------------------------------------------------------------- #
        # ------ Add 10 seconds time sleep (time the song play) before to close the program ------- #
        # ----------------------------------------------------------------------------------------- #
            time.sleep(10)
            while sound.isPlaying():
                exit()
        # --------------------------------------------- #
        # ------ Print this until the time out! ------- #
        # --------------------------------------------- #
        else:
            print("Local current time :", Timer)
            print("\tTimer end at: ", end_time4)
            print("." * 50)
            time.sleep(1)
            its_time = False


first_time_crate()
