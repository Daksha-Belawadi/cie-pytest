def get_student_details():
    name = input("enter student name:")
    program=input("enter program (e.g : BCA/BSc/) : ")
    semester=input("enter semester")

    num_courses = int(input("enter no.of course regidterd:"))


    courses = []
    for i in range(num_courses):
        print(f"\n course {i+1} :")
        course_name = input("course name: ")
        marks = int(input("marks: "))
        courses.append({"course": course_name, "marks": marks}) 

    return {
        "name": name,
        "program": program,
        "semester": semester,
        "courses": courses
    }

def display_details(student):
    print("\n=============student deatils ================")
    print(f"Name: {student['name']}")
    print(f"Program: {student['program']}")
    print(f"Semester:{student['semester']}")
    print("\n Courses & Marks:")

    for c in student["courses"]:
        if c["marks"] < 50:
            print(f"{c['couse']} - {c['marks']}  (failed)")
        else:
            print(f"{c['course']} - {c['marks']}")

    print("=================================================")


if __name__ == "__main__":
    student = get_student_details()
    display_details(student)