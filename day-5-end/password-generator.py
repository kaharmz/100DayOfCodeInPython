import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '>', '<', '|', '-', '_', '@', '=']

char = '''
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
'''

print(char)

print("Welcome to the PyPassword Generator!")
inp_letters = int(input("How many letters would you like in your password?\n"))
inp_symbols = int(input("How many symbols would you like?\n"))
inp_numbers = int(input("How many numbers would you like?\n"))

result = []

for letter in range(inp_letters):
    rnd_letter = random.choice(letters)
    result.append(rnd_letter)

for symbol in range(inp_symbols):
    rnd_symbol = random.choice(symbols)
    result.append(rnd_symbol)

for number in range(inp_numbers):
    rnd_number = random.choice(numbers)
    result.append(rnd_number)

generates = random.sample(result, len(result))
print(f"Here is your password: {''.join(generates)}")

