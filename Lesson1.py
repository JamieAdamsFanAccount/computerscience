import random

# Set variables
userAge = 0;
name = "";
# Set random diologue
diologueOptions = random.randint(1, 2);

# Print different text depending on the random diologue options
if (diologueOptions == 1):
    print("Hello, welcome to my absolutely epic program");
else:
    print("Hello, welcome to this great program");

# Ask user information
name = input("What is your name?");
userAge = int(input("How old are you?"));

# If user is 11 or older
if (userAge >= 11):
    if (diologueOptions == 1):
        print("You're 11 or older!");
    else:
        print("Welcome to the 11 or older club");
else: # If user is younger than 11
    if (diologueOptions == 1):
        print("You're under 11");
    else:
        print("You're too young to join our epic club");
