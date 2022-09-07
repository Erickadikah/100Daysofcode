student_scores = input("input a list of student in height\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
# if int(student_scores[n]) >= 1000:
#     print("highest score.")


print(student_scores)


# print(max(student_scores))
print(f"the higest score in the class is : {(max(student_scores))}")
