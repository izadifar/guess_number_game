import random
goal = random.randint(0,99)
print('Welcome to the Number Guesssing Game!')
print("I'm thinking of a number between 0 and 100.")


level = input('choose a the difficulty. Type \'easy\' or \'hard\': ')

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5

game = True
guess = 100
while game:
    print(f'You have {attempts} attempts remaining to guess the number.')
    geuss = int(input('Make a guess: '))
    if guess > goal:
        print('Too high.')
    elif guess < goal:
        print('Too low.')
    attempts -= 1
    if guess == goal:
        print('You got it! The answer was: {goal}')
        game = False
    elif attempts == 0:
        game = False
        print("You've run out of guesses, you lose.")
