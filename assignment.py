l
student_names = ["Sandra", "Patricia", "Phionah", "Anitah"]
student_marks = [80, 56, 78, 90]

# (a) Print Patricia, Faith, Phionah, and Anitah (note: "Faith" is not in the original list)
print(student_names[1])  # Patricia
print("Faith")            # Add Faith explicitly
print(student_names[2])  # Phionah
print(student_names[3])  # Anitah

# (b) Add Masha at the fourth position (index 3)
student_names.insert(3, "Masha")

# (c) Update the name Phionah to Phionah Aladinah
student_names[2] = "Phionah Aladinah"

# (d) Display the length of the student's list
length_of_students = len(student_names)
print("Length of student names:", length_of_students)

# (e) Print all the student names using a for loop
print("Student Names:")
for name in student_names:
    print(name)

# (f) Calculate the total marks for the student marks variable
total_marks = sum(student_marks)
print("Total Marks:", total_marks)

