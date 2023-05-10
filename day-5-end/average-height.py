# Don't change the code below
student_heights = input("Input a list of student heights: \n ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above

#Instructions
total = 0
result = 0
#You are going to write a program that calculates the average student height from a List of heights.
for student in student_heights:
  total += student
  result += 1
average = total / result
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
print(round(average))
#Write your code below this row