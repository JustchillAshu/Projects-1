from random import randrange
n=int(input("Enter a range to guess: "))
if n<0:
    print("please enter a positive number")
rand_numb=randrange(1,n+1)
while True:
    user_guess=int(input("Guess the number "))
    if user_guess==rand_numb:
        print("You Guess it correctly,the number is ",rand_numb)
        break
    elif user_guess>rand_numb:
        print("You Guessed higher, pls guess a lower number")
    elif user_guess<rand_numb:
        print("You guessed low,please guess a higher number")
print("Thank you for playing")
