# List of friends' names
friends = ["Shreeya", "Rahul", "Ananya", "Riya", "Soham"]

# Create list of tuples
name_length = []

for name in friends:
    name_length.append((name, len(name)))

# Print result
print("List of tuples:")
print(name_length)