import random

#Solution One
random_string = ["Heads", "Tails"]
results = random.choice(random_string)
print(results)

#Solution Two
random_number = random.randint(2, 3)
if random_number == 2:
    print('Heads')
else:
    print('Tails')