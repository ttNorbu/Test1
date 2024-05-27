# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    
    # Add to list and dictionary
    students_list.append(name)
    students_dict[name] = {'age': age, 'grade': grade}
    
    # Success message and print dictionary items
    print(f"Student {name} added successfully!")
    print("Current students:")
    for student in students_dict:
        print(f"{student}: Age - {students_dict[student]['age']}, Grade - {students_dict[student]['grade']}")

# Function to search for a student
def search_student():
    name = input("Enter the name of the student to search: ")
    if name in students_dict:
        print(f"Student found: {name}, Age - {students_dict[name]['age']}, Grade - {students_dict[name]['grade']}")
    else:
        print("Student not found.")

# Function to remove a student
def remove_student():
    name = input("Enter the name of the student to remove: ")
    if name in students_dict:
        del students_dict[name]
        students_list.remove(name)
        print(f"Student {name} removed successfully.")
    else:
        print("Student not found.")

# Main loop
while True:
    action = input("Choose an action: Add (A), Search (S), Remove (R), Quit (Q): ").upper()
    if action == 'A':
        add_student()
    elif action == 'S':
        search_student()
    elif action == 'R':
        remove_student()
    elif action == 'Q':
        print("Exiting the system.")
        break
    else:
        print("Invalid action. Please choose again.")

