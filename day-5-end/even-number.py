# Write your code below this row
total = 0
# calculates the sum of all the even numbers from 1 to 100
for number in range(1, 101):
    # Cek even number
    if number % 2 == 0:
        # add up every even number
        total += number
# print total number
print(total)
