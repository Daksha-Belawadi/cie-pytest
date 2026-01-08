
member_name = input("Enter Member Name: ")
membership_type = input("Enter Membership Type: ")
sessions = int(input("Enter Number of Sessions Attended: "))
fitness_score = float(input("Enter Fitness Score: "))

print("\n--- Gym Membership Details ---")
print("Member Name:", member_name)
print("Membership Type:", membership_type)
print("Sessions Attended:", sessions)
print("Fitness Score:", fitness_score)

if fitness_score < 50:
    print("Status: Needs improvement")
else:
    print("Status: Good fitness level")
