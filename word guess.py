import random
import time



print("""Hi... 
      Welcome to word guess game!
      This is a word guessing game and you should guess word's
      from a list of fruits...""")

time.sleep(3)
print("-------------------------------")
print("""Let's Start the game...""")
time.sleep(1)
print("loading...")
time.sleep(5)
print("--------------------------------")




fruits = ["apple","banana","orange","blueberry","kiwi","lemon","cherry","peach","waternelon","strawberry"]

secret_word = random.choice(fruits)

chars = list(secret_word)
chars.sort()

word_len = len(secret_word)
print("this word have",word_len,"letter")

guess_chance = 10
print("--------------------------------")
print("you have",guess_chance + word_len,"chance to guess the letter's")
   
count = 0

while count < guess_chance + word_len:
    count += 1
    
    guess = input("Enter your guess:")
           
    if guess in chars: 
        print("yes your guess is right")
        print("------------------------")
        chars.remove(guess)
                     
    elif guess not in chars:
        print("no, you wrong!")
        print("------------------------")
        
    if chars == []:
        print("you win\n you did it at",count,"time")
        print("Answer is",secret_word)
        print("You had",(guess_chance + word_len) - count ,"more chances")
        break


while count >= guess_chance + word_len:
    count += 1
    if count == guess_chance + word_len:
        break
    
    elif count > guess_chance + word_len:
        print("------------------------------------")
        print("GAME OVER\n answer was", secret_word)
        break
    
    