student_heights = input("Input a list of student heights: \n ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Instructions
total_index = 0
total_sum = 0

# You are going to write a program that calculates the average student height from a List of heights.
for student in student_heights:
    total_sum += student
    total_index += 1

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
average = total_sum / total_index

print(f"total height = {total_sum}")
print(f"number of students = {total_index}")
print(f"average height = {round(average)}")
