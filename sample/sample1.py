import sys

# Check argument count
if len(sys.argv) != 3:
    print("No values given using default values")
    distance = 10
    time = 5
else:
    # Read arguments
    distance = float(sys.argv[1])
    time = float(sys.argv[2])

# Calculate speed
speed = distance / time

# Print output
print("----- SPEED DETAILS -----")
print("Distance :", distance)
print("Time     :", time)
print("Speed    :", speed)
print("-------------------------")
