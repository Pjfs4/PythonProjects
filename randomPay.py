import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

dimensao = len(names)
number = random.randint(0,dimensao - 1)
print(f"{names[number]} is going to buy the meal today!")