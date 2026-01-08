# Vehicle Speed Monitor

# Accept vehicle details
vehicle_number = input("Enter Vehicle Number: ")
speed = float(input("Enter Speed (km/h): "))

# Display vehicle details
print("\n--- Vehicle Details ---")
print("Vehicle Number:", vehicle_number)
print("Speed:", speed, "km/h")

# Check speed limit
if speed > 80:
    print("Warning: Speed limit exceeded! Slow down.")
else:
    print("Speed is within the safe limit.")