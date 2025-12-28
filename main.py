import time, os 

def skull_animation():
    frames = [
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
    while True:
        for frame in frames:
            os.system('clear')  # Clear screen
            print(frame)
            time.sleep(0.5)
            
def heal_animation(): 
    frames = [
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
    while True:
        for frame in frames:
            os.system('clear')  # Clear screen
            print(frame)
            time.sleep(0.5)


def menu():
    print("="*60)
    print("1. Start animation skull\n2. Start animation heal")
    print("="*60)
    request = str(input("\n>> "))
    if request == "1":
        skull_animation()
    else:
        heal_animation()


if __name__ == "__main__":
    menu()
