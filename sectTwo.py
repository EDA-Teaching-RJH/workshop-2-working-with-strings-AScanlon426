# Excercise 1
Age = int(input("What is your age?"))
if Age >= 18:
    print ("You are an adult")
else:
    print ("You are a child")

# Excercise 2 
import random
number = random.randint(1,10)
answer = int(input("Guess of the number between 1 and 10"))
if answer == number:
    print ("Correct!")
elif answer > number:
    print ("Too high")
else:
    print ("Too low")

#Excerise 3
score = int(input("What was your score?"))
if score >= 90:
    print ("You got an A")
elif score >=80:
    print ("You got a B")
elif score >=70:
    print ("You got a C")
elif score >=60:
    print ("You got a D")
else:
    print ("You got an F")