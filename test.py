# 2. As

# The 'as' keyword is used to create an alias for a module.
import datetime as dt

today = dt.date.today()
print("Today's date is:", today)

# 4. Break

# The 'break' keyword is used to exit a loop when a condition is met.
names = ["Ryy", "Ryan", "Azii", "Izumi"]
search = "Ryy"

for name in names:
    if name == search:
        print(f"{name} found!")
        break
    
# 6. Continue

# The 'continue' keyword is used to skip the rest of the current iteration in a loop.
work_days = ["Monday", "Tuesday", "Holiday", "Thursday", "Friday"]

for day in work_days:
    if day == "Holiday":
        continue  # Skip the rest of the loop for "Holiday"
    print(f"Work scheduled for {day}")  # Print work days

# 10. Else

# The 'else' keyword is used to define the fallback case in an if statement.
weather = "rainy"
if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Carry an umbrella!")

# 14. For

# The 'for' keyword is used to iterate over a sequence.
orders = ["Burger", "Pizza", "Pasta"]

for order in orders:
    print(f"Preparing {order}...")
# 16. Global

# The 'global' keyword allows modification of a global variable inside a function.
score = 0  # Global variable

def increase_score():
    global score  # Use the global variable 'score'
    score += 10  # Increase score by 10

increase_score()  # Call the function to increase the score

# Print the updated score
print("Score:", score) 

# 18. Import

# The 'import' keyword is used to include a module.
import random
dice_roll = random.randint(1, 6)
print("You rolled:", dice_roll)

# 20. Is

# The 'is' keyword checks object identity.
session = None
if session is None:
    print("User not logged in.")


# 22. None

# The 'None' keyword represents the absence of a value.
def get_value():
    return None  # Return None

# Call the function
result = get_value()

# Print the result
print("Result:", result)

# 24. Not

# The 'not' keyword negates a boolean value.
if not False:
    print("This is true")

# 26. Pass

# The 'pass' keyword is used as a placeholder.
def upcoming_feature():
    pass  # This function does nothing for now

# Call the function
upcoming_feature()  # No output, as the function does nothing

# 28. Return

# The 'return' keyword returns a value from a function.
def calculate_total(cart):
    return sum(cart)  # Return the total sum

# Example usage
total = calculate_total([10, 20, 30])  # Call the function
print("Total:", total)  # Output: Total: 60

# 29. True

# The 'True' keyword represents the boolean true value.
is_active = True  # User is active

# Check the status
if is_active:
    print("User  is active.")  # Output: User is active.

# 30. Try

# The 'try' keyword is used for exception handling.
try:
    print("Attempting operation...")
    result = 10 / 0  # This will cause an error
except Exception:
    print("An error occurred")  # Output: An error occurred
# 31. While

# The 'while' keyword creates a loop that runs while a condition is true.
password = ""
while password != "secret":
    password = input("Enter password: ")  # Keep asking for the password
print("Access granted!")  # Output when the correct password is entered

# 32. With

# The 'with' keyword simplifies file handling.
with open("log.txt", "a") as log:
    log.write("New user signed in\n")  # Write to the log file

# 33. Yield

# The 'yield' keyword creates a generator.
def infinite_counter():
    num = 0
    while True:
        yield num  # Yield the current number
        num += 1  # Increment the number

# Create a generator
counter = infinite_counter()

# Print the first 5 numbers
for _ in range(5):
    print(next(counter))  # Outputs: 0, 1, 2, 3, 4
