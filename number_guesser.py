from random import randint

guess = 0
secret_number = randint(1, 100)
name = input('Enter your name: ')

print(f"Okay {name}, I have though of a number between 1 and 100\nYou have 8 guesses")

while guess < 8:
    estimation = int(input("What is the number?: "))
    guess += 1

    if estimation < secret_number:
        print("My number is higher")
    elif estimation > secret_number:
        print("My number is lower")
    else:
        print(f'Congratulations {name}! You have guessed in {guess} attempts')
        break

if estimation != secret_number:
    print(f'You have run out of attempts. The secret number is {secret_number}')