# 1. And

# The 'and' keyword is used for logical AND operations.
age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"
def is_eligible_for_discount(age, is_member):
    return age > 60 and is_member

print(is_eligible_for_discount(age, is_member))

# 3. Assert

# The 'assert' keyword is used for debugging and testing.
def validate_age():
    age = int(input("Enter your age: "))
    assert age >= 18, "Age must be 18 or older!"
    return "Access granted"

print(validate_age())

# 5. Class

# The 'class' keyword is used to define a new class.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

account = BankAccount(int(input("Enter initial balance: ")))
deposit_amount = int(input("Enter deposit amount: "))
print("New balance:", account.deposit(deposit_amount))

# 7. Def

# The 'def' keyword is used to define a function.
def greet_user():
    name = input("Enter your name: ")
    return f"Hello, {name}! Welcome back."

print(greet_user())

# 8. Del

# The 'del' keyword deletes items from a dictionary.
inventory = {"apples": 10, "bananas": 5, "expired_milk": 1}

# Show inventory before deletion
print("Before deletion:", inventory)

# Delete 'expired_milk' from the inventory

del inventory["expired_milk"]

# Show inventory after deletion
print("After deletion:", inventory)

# 9. Elif

def categorize_experience():
    years = int(input("Enter years of training: ")) 
    if years > 10:
        return "S-Class Hero"  # Expert level
    elif years > 5:
        return "A-Class Hero"  # Intermediate level
    else:
        return "B-Class Hero"  # Beginner level

print(categorize_experience())

# 11. Except

# The 'except' keyword is used for handling exceptions.
try:
    filename = input("Enter the file name: ")
    with open(filename) as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found!")

# 12. False

# The 'False' keyword represents the boolean false value.
is_logged_in = False  # User is not logged in

# Check the login status
if is_logged_in:
    print("User  is logged in.")
else:
    print("User  is not logged in.")

# 13. Finally

# The 'finally' block always executes, even if an exception occurs.
try:
    print("Connecting to database...")
    raise ConnectionError("Database offline!")
except ConnectionError:
    print("Connection failed.")
finally:
    print("Closing database connection.")

# 15. From

# The 'from' keyword is used to import specific parts of a module.
from datetime import datetime

event_date = datetime.strptime(input("Enter event date (YYYY-MM-DD): "), "%Y-%m-%d")
print("Upcoming event on:", event_date)

# 17. If

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Access denied!")

# 19. In

# The 'in' keyword is used to check membership in a collection.
anime_characters = ["Naruto", "Saitama", "Goku", "Luffy", "Edward Elric"]
search_character = input("Enter an anime character name: ")
if search_character in anime_characters:
    print(f"{search_character} is in the list of heroes!")
else:
    print(f"{search_character} is not in the list of heroes!")

# 21. Lambda

# The 'lambda' keyword is used to create anonymous functions.
calculate_tax = lambda price: price * 0.08
price = float(input("Enter the price: "))
print("Tax amount:", calculate_tax(price))

# 23. Nonlocal

def outer():
    character_name = "Luffy"  # Initial character name
    def inner():
        nonlocal character_name  # Declare that we want to use the outer variable
        character_name = input("Enter a new name for the character: ")  # Change the character name
    inner()  # Call the inner function to change the name
    return character_name  # Return the updated character name

# Example usage
print("Updated character name:", outer())

# 25. Or

# The 'or' keyword returns true if at least one condition is met.
value = input("Enter yes or no: ").lower()
if value == "yes" or value == "y":
    print("You said yes!")
else:
    print("You didn't say yes.")

# 27. Raise

def set_temperature():
    temp = float(input("Enter the temperature: "))
    if temp < -273.15:
        raise ValueError("Temperature below absolute zero is not possible!")
    return f"Temperature set to {temp}°C"

try:
    print(set_temperature())
except ValueError as e:
    print(e)


# 29. True

# The 'True' keyword represents the boolean true value.
is_active = True
print("User is active?", is_active)

# 31. While

# The 'while' keyword is used to create a loop that runs while a condition is true.
count = int(input("Enter the starting count: "))
while count < 3:
    print(count)
    count += 1

# 32. With

# The 'with' keyword simplifies file handling.
with open("log.txt", "a") as log:
    log.write("New user signed in\n")  # Write to the log file

