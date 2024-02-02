import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



tentativas = 0
while tentativas < 3:
  numero_random = random.randint(0,2)  
  tentativas += 1
  choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
  if choice == "0":
    print(rock)
    print("computer chose:")
    if numero_random == 0:
      print(rock)
      print("tie")
    elif numero_random == 1:
      print(paper)
      print("You loose")
    else:
      print(scissors)
      print("You Win")
  if choice == "1":
    print(paper)
    print("computer chose:")
    if numero_random == 0:
      print(rock)
      print("You Win")
    elif numero_random == 1:
      print(paper)
      print("tie")
    else:
      print(scissors)
      print("You Loose")
  if choice == "2":
    print(scissors)
    print("computer chose:")
    if numero_random == 0:
      print(rock)
      print("You Loose")
    elif numero_random == 1:
      print(paper)
      print("You win")
    else:
      print(scissors)
      print("Tie")


