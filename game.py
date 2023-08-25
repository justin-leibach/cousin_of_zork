# Game for coding bootcamp and for Sam
# Meant to imitate Zork

print('''
                              _
                            ==(W{==========-      /===-
                              ||  (.--.)         /===-_---~~~~~~~~~------____
                              | \_,|**|,__      |===-~___                _,-'`
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _) | ;  ),   __--~~
                    '~~--_/      _-~/- |/ \   '-~ \
                   {\__--_/}    / \\_>-|)<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    | -Tua Xiong    /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
''')

#Welcome message
print("Welcome adventurer, to a land of fantasy and of peril\n"
      "Many have come before you, some are heroes remembered by all\n"
      "inhabitants of this land, but many more whose names have been\n"
      "lost to time. In this land you will be given many choices,\n"
      "sometimes it is simply a choice of which direction to travel,\n"
      "in that case, the cardinal directions of North, South, East and West\n"
      "will do you well. Other times, you will be presented with a choice,\n"
      "and remember, there is always a choice.")

welcome = input("Are you ready to begin?\n").lower()

if welcome == "y" or welcome == "yes":
      room1 = input("You find yourself in near blackness. The room is cold and wet. The floor \n"
                    "is of rough stone. It is utterly silent. At your feet is a compass rose \n"
                    "etched into the stone. The 4 pointed star glows softly and the letters N, S, E and W \n"
                    "sit at the apex of each point. There is a faint light to the west Which way will you go? \n").lower()
      if room1 == "w" or room1 == "west":
          room2 = input('You stumble along the uneven floor towards the light until you come to a door. \n'
                        'Centered on the door is a hand shaped indent, and an inscription that reads \n'
                        '"Place your Hand here adventurer." \n'
                        'Do you want to place your hand?').lower()
          if room2 == "yes" or room2 == "y":
            print('A small needle pricks your hand and a voice booms\n'
                  '"Welcome adventurer. Your bloodline indicates you are of the Zorkian line, \n'
                  'direct decendant of Zork himself! Zork was our greatest hero, and we are in need of another!"')
            name = input("What is your name Adventurer?\n")
            print(f"Welcome {name}, decendent of the mighty Zork, Hero of Heroes. You come at a great time of need, \n"
                  f"a dire situation that words cannot describe")
            room3 = input("Will you help us?").lower()
            if room3 == "yes" or room3 == "y":
                print("Thank you.")
            else:
                print("You are no Zork!")
      elif room1 == "e" or room1 == "east":
          print("You fall endlessly into the void")
      elif room1 == "s" or room1 == "south":
          print("You hear a clunk as the floor shifts beneath your feet and you feel a whoosh\n"
                "from behind you. You realize that it was a door, and you are trapped\n"
                "You hear stone scraping stone, and a sick feeling fills your stomach as you realize\n"
                "what is happening....The walls are closing in around you")
          choice = input("What do you do?\n")
          if choice == "l;akjsdfjoapsjidfop;ajsdnmfasldjfio":
              print("weird choice")
          else:
              choice2 = input("Panic sets in as you try and fail to push against the closing walls\n")
              if choice2 == "laksjdfjiasdfj":
                  print("weirder")
              else:
                  choice3 = input("You are forced to your knees. You begin to involuntarily scream for help\n")
                  if choice3 == ("alksdjfoiasjdfoija"):
                      print("That is super weird")
                  else:
                      choice4 = input("The walls stop. You can barely move in your crunched position.\n"
                                      "The floor glows slightly, and you can make out what appears to be\n"
                                      "a button on the floor. Do you want to press it?\n").lower()
                      if choice4 == "y" or choice4 == "yes":
                          print('The narrator says "Alright. Just restart the program. You get another shot')
                      else:
                          print("You blackout.\n"
                                "The narrator listens to your bones crunch and your organs pop under pressure....GROSS")

else:
      print("You are a terrible adventurer. Choose better")
