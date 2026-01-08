# Employee Salary Checker

# Accept employee details
employee_name = input("Enter Employee Name: ")
employee_id = input("Enter Employee ID: ")
salary = float(input("Enter Salary: "))

# Display employee details
print("\n--- Employee Details ---")
print("Name:", employee_name)
print("Employee ID:", employee_id)
print("Salary:", salary)

# Check salary condition
if salary < 20000:
    print("Message: Salary is less than 20,000")
else:
    print("Message: Salary is 20,000 or more")