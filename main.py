from frames import skull_frames, heal_frames
from time import sleep
from UIhelpers import clear_screen, colors
# Classes and functions for animations  

class Animation:
    def __init__(self, frames, color=colors.RESET, delay=0.4):
        self.frames = frames # list of strings/the frames
        self.delay = delay # seconds between frames
        self.color = color # color for the animation

    def play(self):
        try:
            while True:
                for frame in self.frames:
                    clear_screen() 
                    print(self.color + frame + colors.RESET) 
                    sleep(self.delay) 
        # added keyboard interrupt in case of infinite loop, user can stop with ctrl+c 
        except KeyboardInterrupt:
            clear_screen()
            print("Animation stopped.")
            menu() 


# old functions, replaced with Animation class usage, saved here for future reference
"""while True:
        for frame in frames:
            os.system('clear')  # Clear screen
            print(frame)
            time.sleep(0.5)"""

#----------------------Menu to select animation\Interface----------------------

def menu():
    print("="*60)
    print("1. Start animation skull\n2. Start animation heal\n3. Exit")
    print("="*60)
    request = str(input("\n>> ")).strip()
    if request == "1":
        print("Starting skull animation. Press Ctrl+C to stop.")
        sleep(2)
        Animation(skull_frames, colors.RED).play()
    elif request == "2":
        print("Starting heal animation. Press Ctrl+C to stop.")
        sleep(2)
        Animation(heal_frames, colors.GREEN).play()
    elif request == "3":
        clear_screen()
        print("Exiting program.")
        sleep(1)
        clear_screen()
        exit()
    else:
        print("Invalid input, please try again.")
        menu()


if __name__ == "__main__":
    menu()