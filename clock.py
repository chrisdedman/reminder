from sys import exit
from AppKit import NSSound
import time

its_time = False
while its_time == False:
    its_time = False
    # ------------------------------------------ #
    # ------ Local Time in your country! ------- #
    # ------------------------------------------ #
    Timer = time.asctime(time.localtime(time.time()))
    end_time = "Mon Jun 29 19:00:00 2020"  # European format
    # ------------------------- #
    # ------ Timer Loop ------- #
    # ------------------------- #
    if Timer == end_time:
        its_time = True
        print("It's time to take your puppy out!")
    # ----------------------------- #
    # ------ Prepare Sounds ------- #
    # ----------------------------- #
        sound = NSSound.alloc()
    # ---------------------------------------------------------------------------------------------------- #
    # ------ Here should be your repertory where your songs are, here is default apple repertory! -------- #
    # ---------------------------------------------------------------------------------------------------- #
        sound.initWithContentsOfFile_byReference_('/Library/Audio/Apple Loops/Apple/01 Hip Hop/Afloat Beat.caf', True)
        sound.play()
    # ----------------------------------------------------------------------------------------- #
    # ------ Add 5 seconds time sleep (time the song play) before to close the program -------- #
    # ----------------------------------------------------------------------------------------- #
        time.sleep(10)
        while sound.isPlaying():
            exit()
    # --------------------------------------------- #
    # ------ Print this until the time out! ------- #
    # --------------------------------------------- #
    else:
        print("Local current time :", Timer)
        print("\tTimer end at: ", end_time)
        print("." * 50)
        time.sleep(1)
        its_time = False
