students = {}

while True:
    print("\n1. Add student")
    print("2. Update grade")
    print("3. Show all grades")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added!")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated!")
        else:
            print("Student not found!")

    elif choice == "3":
        if students:
            print("\nAll Student Grades:")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students yet.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")