# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_people = 0
for n in student_heights:
    total_people += 1

total_height = 0
for n in range(0, total_people):
    total_height += student_heights[n]

average_height = total_height / total_people
print(round(average_height))
