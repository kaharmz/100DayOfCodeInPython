# Don't change the code below
student_scores = input("Input a list of student scores: \n ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0
for score in student_scores:
    # If score more than max score, max score together with score
    if score > max_score:
        max_score = score
# print max score
print(f"The highest score in the class is: {max_score}")
