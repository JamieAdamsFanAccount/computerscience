example = input("Which example would you like to run? e.g: 1a, 1excercise, 2a, etc\n");

if example == "1a":
#1a

    print("Hullo world,");

elif example == "1b":
#1b

    print("I am very pleased to meet you");

elif example == "1c":
#1c

    print("This is\na computer program\nthat prints on multiple lines");

elif example == "1excercise":
#1excercise

    print("This is John's first program");

elif example == "2a":
#2a

    name = "Jamie";
    print("Hello " + name);

elif example == "2b":
#2b

    language = "Python";
    print("I'm learning to program in " + language);

    name = "Bob";
    name = "Liz";
    print("Hello " + name);

    name = "Bob";
    name = name + "by";
    print("Hello " + name);

    name = "Bob";
    name = name + name;
    print("Hello " + name);

    name = "Bob";
    name = name + " " + name;
    print("Hello " + name);


elif example == "2c":
#2c

    word1 = "the"
    word2 = "cat"
    word3 = "sat"
    word4 = "on"
    word5 = "mat"

    print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word1 + " " + word5);

elif example == "3a":
#3a
    name = input("What's your name? \n");
    print("Hello " + name + "!");

    livingarea = input("Where do you live? \n");
    print("I love... the people in " + livingarea + "!");


elif example == "3b":
#3b
    firstname = input("What's your first name? \n");
    lastname = input("What's your last name? \n");
    name = firstname + " " + lastname;

    print("Hello " + name + "!");


elif example == "3c":
#3c
    name = input("What's your name? \n");
    print("Hello " + name + " " + name + " " + name + " " +  name + " " +  name + "!");


elif example == "4a":
#4a
    print(1+6);
    print(7-5);
    print(3*9);
    print(7/2);

elif example == "4b":
#4b
    print(9+9);
    print(5-3);
    print(8*3);
    print(21/3);

    a = 9 + 9;
    b = 5 - 3;
    c = b + a;

    print(c);


elif example == "4c":
#4c
    a = 7;
    b = 8;
    c = a + b;
    print (c);


elif example == "5a":
#5a
    a = int(input("Enter number 1: \n"));
    b = int(input("Enter number 2: \n"));
    c = a + b;
    print ("Both numbers together are " + str(c));

elif example == "5b":
#5b
    width = int(input("Enter width: \n"));
    height = int(input("Enter height: \n"));
    area = width * height;
    print ("The area is " + str(area));

elif example == "5c":
#5c
    pi = 3.14;
    r = float(input("Radius: "));
    h = float(input("Height: "));
    volume = pi*r*r+2*pi*r*h;
    print(volume);

elif example == "6a":
#6a
    city = input("What is the capital of the United Kingdom? \n");
    if city == "London":
        print("Well done")
    elif city == "Brighton":
        print("Correct country but the wrong city")
    elif city == 'F':
        print("Terrible joke and wrong answer, you're not funny don't play no games.")
    else:
        print('Sorry wrong answer')


elif example == "6b":
#6b
    one = int(input("Please enter number 1: "))
    two = int(input("Please enter number 2: "))
    three = int(input("Please enter number 3: "))
    if (one == two and two == three):
        print("SNAP!")
    else:
        print("They do not all match")

elif example == "6c":
#6c
    mark = int(input("What percentage did you get?\n"));
    if (mark > 69):
        grade = "A"
    elif (mark > 59):
        grade = "B"
    elif (mark > 49):
        grade = "C"
    elif (mark > 39):
        grade = "D"
    else:
        grade = "U"
    print("You got the grade: " + grade);

elif example == "7":
#7
    # This is a lovely comment
    print("For legal reasons I have to show this message");

elif example == "8a":
#8a
    for i in range(0, 15):
        print("Computing");
elif example == "8b":
#8b
    letter = input("Please enter a letter:\n");
    number = int(input("Please enter a number:\n"));

    for i in range(0, number):
        print(letter);
elif example == "8c":
    number = int(input("Please enter a number:\n"));

    for i in range(1, 10):
        print(str(i) + " times " + str(number) + " is " + str(number * i));
elif example == "9a":
    userpassword = "";
    password = "jamie";
    while userpassword != "jamie":
        userpassword = input("Enter password \n");
        if userpassword == password:
             print("Welcome")
        else:
             print("Access denied!");
elif example == "9b":
    number = 0;
    while number * number < 5000:
        print(number * number);
        number = number + 1;
elif example == "9c":
    import random;
    x = random.randint(1, 100);
    guessed = 0;
    guesscount = 0;
    print("ey I'm thinking of a number between 1 and 100, you MUST guess it.");
    while guessed == 0:
        guesscount = guesscount + 1;
        guess = int(input("What do you think the number is\n"))
        if (guess > x):
            print("No. The number I'm thinking of is less than " + str(guess))
        elif (guess < x):
            print("No. The number I'm thinking of is larger than " + str(guess))
        elif (guess == x):
            print("You guessed the number! You did it in " + str(guesscount) + " guesses.")
            guessed = 1;
elif example == "10a":
    def circleArea(radius):
        return float(3.14 * radius * radius);
    circle = float(input("Enter a number\n"));
    print(circleArea(circle));
elif example == "10b":

    def triangle(h):
        tri = "*";
        h1=h-1;
        for i in range(0, h):
            print((" "*h1)+tri)
            tri="*"+str(tri)+"*"
            h1=h1-1
    h2=int(input("Triangle length:\n"))
    triangle(h2)

elif example == "11a":
    stop = 1;
    names = [];
    while(stop == 1):
        name = str(input("Please enter a name: "));
        if (name != "END"):
            names.append(name);
        else:
            print("You've entered " + str(len(names)) + " names\n" + str(names));
            stop = 0;

elif example == "11b":
    import random;
    winner = random.randint(0, 4);
    names = [];
    for i in range(0, 5):
        name = str(input("Please enter a name: "));
        names.append(name)
    print("Congratulations, " + str(names[winner]) + "\nYou're the winner!")

elif example == "11c":
    import math
    for n in range(2, 10000):
        prime = 1;
        for i in range(2, 10000):
            if i < n:
                if n%i==0:
                    prime = 0;
        if prime == 1:
            print (n)

elif example == "12a":
    sentence = 'The cat sat on the mat.'
    for letter in sentence:
        print(letter)
elif example == "12b":
    sentence = 'The cat sat on the mat.'
    numberOfA = 0;
    for letter in sentence:
        if letter == "a":
            numberOfA = numberOfA + 1
        print(letter)
    print("There are " + str(numberOfA) + " lowercase A's in the sentence.")
elif example == "12c":
    while (1):
        word = input("Word: ");
        if str.capitalize(word[::-1]) == str.capitalize(word): # Should be spelt capitalise
            print ("This is a palindrome")
        else:
            print ("This is not a palindrome")
elif example == "13a":
    fileToOpen = input("What file should I open?")
    myFile = open(fileToOpen, 'rt')
    contents = myFile.read();
    contents = contents.split();
    n = 0;
    for val in contents:
        n = n + int(val);
    print(n / len(contents))
    myFile.close()

elif example == "13b":
    stop = 1;
    names = [];
    while(stop == 1):
        name = str(input("Please enter a name: "));
        if (name != "END"):
            names.append(name);
        else:
            print("You've entered " + str(len(names)) + " names\n" + str(names));
            fileToOpen = input("What file should I write this to?")
            myFile = open(fileToOpen, 'wt')
            myFile.write(str(names))
            myFile.close()
            stop = 0;

elif example == "13c":
    import os
    import sqlite3
    online = 1;
    con = sqlite3.connect('test.db')
    cur = con.cursor();
    
    
    fileDirectory = "./database/"
    def checkname(name):
        cur.execute("select * from leaderboard where name=:name", {"name": name});
        contents = cur.fetchone();
        if contents is not None:
            return contents[2];
        else:
            return "User not in database.";
        

    def writename(name):
        # name = name.lower();
        # fileToOpen = fileDirectory + name + ".txt";
        # myFile = open(fileToOpen, 'wt');
        score = input("What was their score?");
        # contents = myFile.write(name + " " + str(score));
        cur.execute("INSERT INTO leaderboard (name, score) values(\"" + name + "\", " + score + ")");
        con.commit();
        return "Okay we did write that";
        
    # def highest():
    #     for filename in os.listdir(fileDirectory):
    #         for a in checkname(filename.replace(".txt", "")):
    #             if (a.isdigit()):
    #                 print
    # haha sex number
    #

    while (online == 1):
        checkOrWrite = input("Are you checking a score or writing a score (c/w)");
        if checkOrWrite == "c":
            nameToCheck = input("What name should I check \n");
            print(checkname(nameToCheck))
        elif checkOrWrite == "w":
            nameToWrite = input("What name should I write \n");
            print(writename(nameToWrite))
        elif checkOrWrite == "kill":
            con.close()
            online = 0;
            
else:
    print("That example was not found");