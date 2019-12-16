secret = 22
guess = 0

while guess != secret:
    guess = int(input("Rate meine Zahl "))
    if (guess == secret):
        print("Richtig.")
    else:
         if (guess>secret):
            print("die Zahl ist niedriger")
         else
            print("die Zahl ist höher")
         print("versuche es nochmal")
