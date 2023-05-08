#Don't change the code below
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#Don't change the code above

#Write your code below this row
#Cek position input index 0
column = int(position[0])

#Cek position input index 1
row = int(position[1])

#mapping column and row, and change with 'X'
map[row - 1][column - 1] = 'X'
#Write your code above this row

#Don't change the code below
print(f"{row1}\n{row2}\n{row3}")