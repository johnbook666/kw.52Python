import random

guess = 0
secret = random.randint(1, 10)

while True:
    guess = int(input("Rate meine Zahl "))
    if (guess == secret):
        print("Richtig.")
        break
    elif (guess > secret):
            print("deine geratene Zahl ist größer")
    elif (guess < secret):
            print("deine geratene Zahl  ist niedriger")
    print("versuche es nochmal")