"""Write a script that does the following:
Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades.
 Use this input to create lists for names, assignments, and grades.
Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to
 two times the number of missing assignments."""

names_input = input("Names: \n")
names = names_input.split(",")
assignments_input = input("Assignments: \n")
assignments = assignments_input.split(",")
grades_input = input("Grades: \n")
grades = grades_input.split(",")
final_grades = []

for i in range(len(assignments)):
    final_grades.append(int(assignments[i]) * 2 + int(grades[i]))
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(names)):
    print(message.format(names[i], assignments[i], grades[i], final_grades[i]))

