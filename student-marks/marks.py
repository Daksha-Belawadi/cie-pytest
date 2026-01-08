# student_marks.py

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

sub1 = int(input("Enter marks in Subject 1: "))
sub2 = int(input("Enter marks in Subject 2: "))
sub3 = int(input("Enter marks in Subject 3: "))

print("\n--- Student Details ---")
print("Name:", name)
print("Roll Number:", roll_no)

print("\n--- Subject Marks ---")
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)

print("\n--- Subjects Scoring Below 50 ---")
if sub1 < 50:
    print("Subject 1")
if sub2 < 50:
    print("Subject 2")
if sub3 < 50:
    print("Subject 3")

if sub1 >= 50 and sub2 >= 50 and sub3 >= 50:
    print("None")