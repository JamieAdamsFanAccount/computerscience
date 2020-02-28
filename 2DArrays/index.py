import random;

gamemap = [[0 for x in range(10)] for y in range(10)]
gamemap[6][3] = 1;
position = [random.randint(0, 9)][random.randint(0, 9)];

print(position)
gamemap[position] = 1; 

won = false;
guess = [];

def guess():
    guess = guess[int(input("Where do you think X is?")), int(input("Where do you think Y is?"))]
    if (guess == position):
        print("You got it!");
    else:
        guess();

guess();



