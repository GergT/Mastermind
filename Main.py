#imports and some variables
import random
import pygame, sys
from pygame.locals import QUIT
loop = False

#RGB colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,128,0)
PINK = (255,0,127)

#Peg sizes
CWIDTH = 50
CHEIGHT = 50
BWIDTH = 20
BHEIGHT = 20

#The raw mastermind program
class Mastermind:
  def __init__(self):
    self.colours = ['R', 'G', 'B', 'Y',"O","P"]
    self.code = self.generate_code()
    self.turns = 0
    self.game_over = False

  #gets user input
  def get_guess():
    guess = input("Enter your guess (4 colours from r, g, b, y, o, p): ")
    return guess

  #creates the code that you have to guess
  def generate_code(self):
    loco = ""
    for p in range (4): 
      loco = loco + random.choice(self.colours) 
    return loco
    
  #Checks how correct the guess is
  def get_feedback(self, guess):
    tempfeed = []
    feedback = ""
    for x in range(len(guess)):
      if guess[x].upper() == self.code[x].upper():
        tempfeed.append('b')
      elif guess[x].upper() in self.code.upper():
        tempfeed.append('w')
    random.shuffle(tempfeed)
    for x in range(len(tempfeed)):
      if tempfeed[x] == 'b':
        pygame.draw.rect(DISPLAYSURF,BLACK,(385+30*x,35+self.turns*100,BWIDTH,BHEIGHT))
      elif tempfeed[x] == 'w':
        pygame.draw.rect(DISPLAYSURF,WHITE,(385+30*x,35+self.turns*100,BWIDTH,BHEIGHT))        
      feedback = feedback + tempfeed[x]
    return feedback

  #Converts the letters (representing colours) into colour emojis
  def colour_convert(self,guess):
    display_guess = ""
    for x in range (4):
      if guess[x].upper()== "R":
        pygame.draw.rect(DISPLAYSURF,RED,(25+(100*x),(25+self.turns*100),CWIDTH,CHEIGHT))
      if guess[x].upper()== "B":
        pygame.draw.rect(DISPLAYSURF,BLUE,(25+(100*x),(25+self.turns*100),CWIDTH,CHEIGHT))      
      if guess[x].upper()== "G": 
        pygame.draw.rect(DISPLAYSURF,GREEN,(25+(100*x),(25+self.turns*100),CWIDTH,CHEIGHT))
      if guess[x].upper()== "Y":  
        pygame.draw.rect(DISPLAYSURF,YELLOW,(25+(100*x),(25+self.turns*100),CWIDTH,CHEIGHT))      
      if guess[x].upper()== "O": 
        pygame.draw.rect(DISPLAYSURF,ORANGE,(25+(100*x),(25+self.turns*100),CWIDTH,CHEIGHT))      
      if guess[x].upper()== "P":
        pygame.draw.rect(DISPLAYSURF,PINK,(25+(100*x),(25+self.turns*100),CWIDTH,CHEIGHT))    
    pygame.display.update()


  #the process of running the game
  def play(self):
    while not self.game_over:
      guess = input("Enter your guess (4 colours from r, g, b, y, o, p): ")
      self.get_feedback(guess)
      self.colour_convert(guess)
      self.turns = self.turns +1
      if guess.upper() == self.code.upper():
        print("Congratulations! You've guessed the correct code.")
        self.game_over = True
        global loop
        loop = True     
      elif self.turns == 6:
        print("You lost! You did not crack the code within 6 attempts")
        self.game_over = True
        loop = True
      else:
        print("You have", (6-self.turns), "turns left.")
#          

#running the pygame board
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Mastermind')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((102,51,0))
    pygame.display.update()
    
    while not loop:
      game = Mastermind()
      game.play()
