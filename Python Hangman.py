from turtle import *
from random import randint
import time


wordList = ['abberation', 'grusome', 'fatuous', \
  'fantastic', 'coverage', 'victorious', \
  'inaugurate', 'outgoing', 'accurate', 'shameful']
  
sw = 500
sh = 500
s=getscreen()
s.setup(sw,sh)
s.bgcolor('#012051')
t=getturtle()
t.color(255, 255, 255)
t.width(8)
t.hideturtle()
#t.forward(100)


tWriter = Turtle()
tWriter.color(255, 255, 255)
tWriter.hideturtle()




tBadLetters = Turtle()
tBadLetters.hideturtle()


alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayWord = ""
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
fails = 6
fontS = int(sh*0.05)
gameDone = False


def displayText(newText):
  tWriter.clear()
  tWriter.color("white")
  tWriter.penup()
  tWriter.goto(-int(sw*0.45),-int(sh*0.33))
  tWriter.write(newText, font=('Arial',fontS, 'bold'))
  
def displayBadLetters(newText):
  tBadLetters.clear()
  tBadLetters.color("red")
  tBadLetters.penup()
  tBadLetters.goto(-int(sw*0.44), int(sh*0.40))
  tBadLetters.write(newText, font=('Arial',fontS, 'bold'))


def chooseWord():
  global secretWord
  secretWord = wordList[randint(0,len(wordList)-1)]
  print("The secret word is:" + secretWord)
  
def makeDisplay():
  global displayWord, secretWord, lettersCorrect
  displayWord = ""
  for letter in secretWord:
    if letter in alpha:
      if letter.lower() in lettersCorrect.lower():
        displayWord += letter + " "
      else:
        displayWord += "_" + " "
    else:
      displayWord += letter + " "
    
def getGuess():
  boxTitle = "Letters Used: " + lettersWrong
  guess = input("Enter a guess or type $$ to guess the word")
  return guess
  
def updateHangmanPerson():
  global fails
  if fails == 5:
    drawHead()
  if fails == 4:
    drawTorso()
  if fails == 3:
    drawRightleg()
  if fails == 2:
    drawLeftleg()
  if fails == 1:
    drawLeftarm()
  if fails == 0:
    drawRightarm()
  
def checkWordGuess():
  global gameDone, fails
  boxTitle = "Guess the Word!"
  guess = input("Enter your guess for the word")
  if guess.lower == secretWord.lower:
    displayText("Yes! " + secretWord + " is the word!")
    gameDone = True
  else:
    displayText("No! " + guess + " is not the word!")
    time.sleep(1)
    displayText(displayWord)
    fails -=1
    updateHangmanPerson()


def playGame():
  global fails, lettersCorrect, lettersWrong, alpha, gameDone
  while gameDone == False and fails > 0 and "_" in displayWord:
    theGuess = getGuess()
    if theGuess == "$$":
      checkWordGuess()
    elif len(theGuess) > 1 or theGuess == "":
      displayText("No" + theGuess + " only one letter please")
      time.sleep(1)
      displayText(displayWord)
    elif theGuess not in alpha:
      displayText("No " + theGuess + " is not a letter")
      time.sleep(1)
      displayText(displayWord)
    elif theGuess.lower() in secretWord.lower(): 
      lettersCorrect += theGuess.lower()
      makeDisplay()
      displayText(displayWord)
    elif theGuess.lower() not in lettersWrong.lower():
      displayText("No! " + theGuess + " is not the word!")
      time.sleep(1)
      lettersWrong += theGuess.lower() + ", "
      displayBadLetters("Not in word: {" + lettersWrong + "}")
      displayText(displayWord) 
      fails -=1
      updateHangmanPerson()
    else:
      displayText("No " + theGuess + " is already guessed")
      time.sleep(1)
      displayText(displayWord)
      
    if fails <= 0:
      displayBadLetters("No more Guesses")
      displayText("You lose, word is " + secretWord)
      gameDone = True
    if "_" not in displayWord: 
      displayBadLetters("You Win, word is " + secretWord)
      
      
      


def drawGallows():
  t.penup()
  t.goto(-int(sw*0.25), -int(sh*0.25))
  t.pendown()
  t.forward(int(sw*0.6))
#pole
  t.backward(int(sw*0.1))
  t.left(90)
  t.forward(int(sh*0.6))
#top
  t.left(90)
  t.forward(int(sw*0.3))
#noose
  t.left(90)
  t.forward(int(sh*0.05))
  
def drawHead():
  hr = int(sw*0.06)
  t.penup()
  t.goto(t.xcor()-hr, t.ycor()-hr)
  t.pendown()
  t.circle(hr)
#set up for body
  t.penup()
  t.showturtle()
  t.goto(t.xcor()+hr, t.ycor()-hr)
#torso
def drawTorso():
  t.pendown()
  t.forward(int(sw*0.16))
  
def drawRightleg():
  t.left(30)
  t.forward(70)
  t.left(180)
  t.forward(70)
  
def drawLeftleg():
  t.left(120)
  t.forward(70)
  t.left(180)
  t.forward(70)
  t.left(30)
  
def drawLeftarm():
  t.forward(40)
  t.left(90)
  t.forward(55)
  t.left(180)
  
def drawRightarm():
  t.forward(110)
  
tWriter = Turtle()
tWriter.hideturtle()




#program starts here
drawGallows()
drawHead()
drawTorso()
drawRightleg()
drawLeftleg()
drawLeftarm()
drawRightarm()


time.sleep(1)
t.clear()
drawGallows()
chooseWord()
displayText("have a nice day")
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word: {" + lettersWrong + "}")
playGame()