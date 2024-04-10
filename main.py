def process_grade():
    '''loops until a grade is given within range of 0 to 100
    when an appropriate grade is given then the function returns it'''
    while True:
        try:
            grade = float(input("What is the student's grade?\n"))
            if not 0 <= grade <= 100:
                raise ValueError("Grade must be between 0 and 100")
            return grade
        except ValueError:
            print("Invalid grade. Please enter a number between 0 and 100\n")

def process_name():
    '''loops until the name input contains only characters from the english alphabet and spaces'''
    while True:
        name = input("What is the student's name?\n").lower()
        if all(char.isalpha() or char.isspace() for char in name):
            return name
        else:
            print("Invalid name. Please enter a valid name containing only alphabets and spaces.\n")

def process_input():
    '''returns a dictionary with score and name values that are returned from their respective functions'''
    name = process_name()
    grade = process_grade()
    return {"name": name, "grade": grade}

def keep_going():
    '''loops until the input is either yes or no and returns false only when the user wants to stop the loop in order
    to advance to the next stage of the grading system process'''
    while True:
        choice = input("Do you want to continue adding students' grades? (yes/no)\n").lower()
        if choice in ("no", "n"):
            return False
        elif choice in ("yes", "ye", "y"):
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.\n")

def calculate_grade_result(grade):
    '''returns the grade based on the supplied score'''
    if grade < 40:
        return "Fail"
    elif grade < 50:
        return "Pass"
    elif grade < 60:
        return "2:2"
    elif grade < 70:
        return "2:1"
    else:
        return "Honours"

def main():
    student_data = []
    while True:
        student_data.append(process_input())
        if not keep_going():
            break

    student_grades = []
    for student in student_data:
        grade_result = calculate_grade_result(student["grade"])
        student_grades.append({"name": student["name"].title(), "grade": grade_result, "score": student["grade"]})

    for student in student_grades:
        if student["grade"] == "Fail":
            print(f"{student['name']} failed the course with a score of {student['score']:.2f}/100")
        else:
            print(f"{student['name']} got a {student['grade']}. They had a score of {student['score']:.2f}/100")

if __name__ == "__main__":
    main()