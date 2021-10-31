import time 

#Different User Response References

yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Objects to be grabbed
sword = 0
flower = 0

#Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  rock = ["ROCK" "Rock" "rock" "rOCK"]
  wait = ["WAIT" "Wait" "wait" "waiT"]
  run =  ["Run" "run"]




  print ("After an accident at sea with a strong storm"
  ", you fall off your hiatus and wake up on a beach in the morning"
   "with a huge headache and very disoriented."
  " You struggle to understand where you are and what happened,"
  "but you are interrupted when you hear something coming out of the water and coming towards you."
  "A tipe of sea monster is running towards you. You will :")
  time.sleep(1)
  print ("""  TO GRAB A NEARBY ROCK AND THROW IT AT THE MONSTER: TIPE (ROCK)
  B. TO LIE DOWN AND WAIT TO BE ATTACKED: TIPE (WAIT)
  C. RUN""")
  choice = input(">>> ") #Here is your first choice.
  if choice in rock:
    option_rock()
  elif choice in wait:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  elif choice in run:
    option_run()
  

def option_rock(): 
  run =  ["Run" "run"]
  rock = ["ROCK" "Rock" "rock" "rOCK"]
  cave =["Cave" "Cave" "cave"]


  print ("\nThe moster is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. RUN
  B. THROW ANOTHER ROCK
  C. RUN TOWARDS A NEARBY CAVE""")
  choice = input(">>> ")
  if choice in run:
    option_run()
  elif choice in rock:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "monsters head. You missed. \n\nYou died!")
  elif choice in cave:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\nYou were hesitant, since the cave was dark and "
  "ominous. Before you fully enter, you notice a shiny sword on "
  "the ground. Do you pick up a sword. Yes/N?")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. HIDE IN SILENCE
  B. FIGHT
  C. RUN""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? But what if"
    " the monster can see in the dark?, right? Not sure, but "
    "I'm going with YES, so...\n\nYou died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou laid in wait. The shimmering sword attracted "
    "the monster, which thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the monster "
    "reached out to grab the sword, you pierced the blade into "
    "its chest. \n\nYou survived!")
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the monster enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the monster turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the monster's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. HIDE BEHIND BOULDER
  B. TRAPPED, SO YOU FIGHT
  C. RUN TOWARDS AN ABANDONED TOWN""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an monster. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the monster to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending monster.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the monster. It does! The monster was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()