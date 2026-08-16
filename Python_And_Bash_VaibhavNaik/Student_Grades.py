students = {
    "Rahul": "A",
    "Priya": "B",
    "Amit": "C"
}

name = input("Enter student name: ")
grade = input("Enter grade: ")

if name in students:
    students[name] = grade
    print("Student grade updated successfully.")
else:
    students[name] = grade
    print("New student added successfully.")

print("\nStudent Grades:")

for student, grade in students.items():
    print(student, ":", grade)