#Generate a random number
#Ask the user to make a guess
#If user type a str say not a number
#make a gap of number 1-100
import random

number_to_guess=random.randint(1, 100)
while True:
 try:
       guess= int(input("Guess the number between 1 and 100: "))
       if guess < number_to_guess:
         print("Too low!")
       elif guess > number_to_guess:
            print("To high!")
       else:
            print("Congratulations! You gessed the number.")
            break


 except ValueError:  
      print("Plese enter a valid number")

