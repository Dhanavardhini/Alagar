import random

   secret_number = random.randint(1, 100)
   attempts = 0

   print("Guess the number between 1 and 100.")

   while True:
       guess = int(input("Enter your guess: "))
       attempts += 1

       if guess == secret_number:
           print(f"Congratulations! You guessed the number in {attempts} attempts.")
           break
       elif guess < secret_number:
           print("Try higher.")
       else:
           print("Try lower.")