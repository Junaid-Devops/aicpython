age = int(input("Enter your age: "))

# Determine stage based on the age
if age >= 0 and age <= 1:
    stage = "infant"
elif age > 1 and age <= 3:
    stage = "toddler"
elif age > 3 and age <= 12:
    stage = "child"
elif age > 12 and age <= 19:
    stage = "teenager"
elif age >= 20:
    stage = "adult"

print(stage)