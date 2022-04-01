import random

print("Welcome to the Oregon Trail, traveler! Your options are: travel/hunt/rest/status/command/quit")

def update_days (number_of_days):
  while(number_of_days > 0):
    add_day()
    number_of_days = number_of_days - 1 
 
def add_day():
  global food
  global day1
  global day2
  global hp
   
  food = food - 5 
  
  global curr_month
  global curr_day
  global MONTHS_WITH_31_DAYS
   
  if day1 == curr_day or day2 == curr_day:
    #hp goes down by 1 
    hp = hp - 1 
    
  if curr_month in MONTHS_WITH_31_DAYS and curr_day == 31:
    curr_day = 1
    curr_month = curr_month + 1 
  elif curr_month == 30:
    curr_day = 1
    curr_month = curr_month + 1 
  else:
    curr_day = curr_day + 1 

def travel():
  global miles_left
  miles_left = miles_left - (random.randint(30,60))
  update_days(random.randint(2,5))
  
def rest():
  global hp 
  hp = hp + 1
  update_days(random.randint(2,5))
  
def hunt():
  global food 
  food = food + 100 
  update_days(random.randint(2,5))
  
def status():
  print("Health: ", hp)
  print("Food: ", food)
  print("Miles left: ", miles_left)
  print("Today's Date: " + str(curr_month) + "/" + str(curr_day))

def help():
  print("Your options are: travel/hunt/rest/status/command/quit")
  
def quit():
  return game_over == False 

hp = 5
day1 = 3
day2 = 26
food = 500
miles_left = 2000
curr_day = 1
curr_month = 3
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
game_over = False
user_name = str(input("What is your name, traveler? "))

while(game_over == False):
  
  user_input = str(input("What do you want to do? "))
  
  if user_input == "travel":
    travel()
  
  elif user_input == "rest":
    rest()
 
  elif user_input == "hunt":
    hunt()
  
  elif user_input == "status":
    status()
  
  elif user_input == "help":
    help()
  
  elif user_input == "quit":
    game_over = quit()
  
  else:
    print("That is not an option.")
  
  if (food <= 0 or hp <= 0 or curr_day >= 31 and curr_month >= 12):
    game_over == True 
    print("You failed.")
  elif miles_left <= 0:
    print("You got to Oregon! Congratulations!")
