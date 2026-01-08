def get_student_details():
    name = input("Enter student name: ")
    reg_no = input("Enter register number: ")
    total_marks = int(input("Enter total marks: "))

    return {
        "name": name,
        "reg_no": reg_no,
        "marks": total_marks
    }


def display_result(student):
    print("\n========== STUDENT DETAILS ==========")
    print(f"Name           : {student['name']}")
    print(f"Register No    : {student['reg_no']}")
    print(f"Total Marks    : {student['marks']}")

    if student['marks'] < 50:
        print("Result         : Fail")
    else:
        print("Result         : Pass")

    print("====================================")


if __name__ == "__main__":
    student = get_student_details()
    display_result(student)