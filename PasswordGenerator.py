#Password Generator
import random
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
simbolos = ["!", "@", "#", "%", "$", "/", "(", ")", "=",
            "?", "+", "*", "-"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print("Welcome to the PyPassword Generator!")
letters = input("How many letters would you like in your password?\n")
symbols = input("How many symbols would you like?\n")
numbers = input("How many numbers would you like?\n")

password_list = []
letra_a_escolher = ""
for let in range(1, int(letters) + 1):
    password_list.append(random.choice(letras))
simbolo_a_escolher = ""
for symb in range(1, int(symbols) + 1):
    password_list.append(random.choice(simbolos))
numero_a_escolher = ""
for num in range(1, int(numbers) + 1):
    password_list.append(random.choice(numeros))
random.shuffle(password_list)
password = ""
for i in password_list:
    password += i

print(f"Your password is {password}")