import time, os # used for delay and clearing screen, might nick pick functions later
# Classes and functions for animations  
class Animation:
    def __init__(self, frames, delay=0.4):
        self.frames = frames # list of strings/the frames
        self.delay = delay # seconds between frames

    def play(self):
        try:
            while True:
                for frame in self.frames:
                    os.system('clear')  # Clear screen
                    print(frame)
                    time.sleep(self.delay) # basic delay between frames/fps
        # added keyboard interrupt in case of infinite loop, user can stop with ctrl+c 
        except KeyboardInterrupt:
            os.system('clear')
            print("Animation stopped.")
            menu() 

# ----------------------Frames for different animations----------------------

"""Skull Animation, will use this for a death screen or a boss battle depending on the situation"""          
skull_frames = [
        '''                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
             $$u$ $ $ $ $u$$
              $$$$$u$u$u$$$
  uuu          "$$$$$$$$$"         uuu
 u$$$$            """"            u$$$$
  $$$$$uu                      uu$$$$$$
u$$$$$$$$$$$uu             uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$
                YOU DIED!
                MUHAHAHA!
            Killed by (placeholder)!
            Level reached: (placeholder)
            
            ''',
        '''                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
             $             $
              $           $
  uuu         $u$ $ $ $ $u$        uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$
                YOU DIED!
                MUHAHAHA!
            Killed by (placeholder)!
            Level reached: (placeholder)
            
            '''
    ]

# heal frames for a healing spell or potion use, could be used in various contexts, might improve later         
heal_frames = [
        '''        __    
     __|  |__
    |__    __|          /\\
       |__|            /  \\
              ____     \\  /
             |    |     \\/
         ____|    |____
        |              |
        |____      ____|
             |    |     
             |____|
        
        Healing .
            ''',
        '''       ____                  
      |    |
  ____|    |____
 |              |
 |____      ____|
      |    |      /\\
      |____|     /  \\
                 \\  /
            __    \\/
         __|  |__
        |__    __|
           |__|
        Healing . .
            '''
    ]
# old functions, replaced with Animation class usage, saved here for future reference
"""while True:
        for frame in frames:
            os.system('clear')  # Clear screen
            print(frame)
            time.sleep(0.5)"""

#----------------------Menu to select animation\Interface----------------------

def menu():
    print("="*60)
    print("1. Start animation skull\n2. Start animation heal")
    print("="*60)
    request = str(input("\n>> "))
    if request == "1":
        Animation(skull_frames).play()
    else:
        Animation(heal_frames).play()


if __name__ == "__main__":
    menu()