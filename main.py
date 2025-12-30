from asyncio import run
from frames import skull_frames, heal_frames
from time import sleep
from UI.UIhelpers import clear_screen, colors
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
            
class Menu():
    def __init__(self, title, options):
        self.title = title
        self.options = options
    def display(self):
            print(self.title)
            for i, option in enumerate(self.options, start=1):
                print(f"{i}. {option}")
    def run(self):
        self.display()
        choice = input("Select an option: ")
        if choice == '1':
            print("Starting Skull Animation. Press Ctrl+C to stop.")
            sleep(2)
            Animation(skull_frames, color=colors.RED, delay=0.5).play()
        elif choice == '2':
            print("Starting Heal Animation. Press Ctrl+C to stop.")
            sleep(2)
            Animation(heal_frames, color=colors.GREEN, delay=0.3).play()
        elif choice == '3':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.run()


# old functions, replaced with Animation class usage, saved here for future reference
"""while True:
        for frame in frames:
            os.system('clear')  # Clear screen
            print(frame)
            time.sleep(0.5)"""

#----------------------Menu to select animation\Interface----------------------


if __name__ == "__main__":
    Menu("Select Animation", ["Skull Animation", "Heal Animation", "Exit"]).run()