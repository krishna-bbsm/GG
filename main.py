from random import randint #import randint to generate an automatic secret number
# initiate level 1
level = 1
points = [100,75,50,25,10]  #sequence type to store points
points_scored = list()  #sequence type to store points scored at each level
#loop for 3 stages
while level <= 3:
    end_value = level * 10  #complexity range for each stage
    secret_number = randint(1,end_value) #secret number generation
    #looping statement for 5 attempts at each stage
    for counter in range(0,5):
        guess_number = int(input("Guess the secret number between 1 and {} ({} attempts left):".format(end_value,5-counter)))
        if secret_number == guess_number:
            print("Your Guess is Correct, You Won the level {} with {} points".format(level,points[counter]))
            points_scored.append(points[counter])#add the point scored in this stage into the list
            level = level + 1
            break
        elif guess_number < secret_number:
            print("Your Guess is lower than secret number")
        else:
            print("Your Guess is higher than secret number")
    else:
        print("Game Over, You Loose the Game, secret number is {}".format(secret_number))
        break
else:
    print("Congratz, You Won the Game with {} !!!".format(sum(points_scored)))
    #loop to display scored points in every stage
    for i in range(0,3):
        print("level {} points {}".format(i+1, points_scored[i]))