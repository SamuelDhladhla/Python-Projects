print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What is the output of this list comprehension: [(x, y) for x in range(3) for y in range(3)]?")
if answer == "[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]":
    print('Correct!')
    score += 1
else :
    print("Incorrect!")

answer = input("Which keyword is used in Python to catch exceptions? ")
if answer == "except":
    print('Correct!')
    score += 1
else :
    print("Incorrect!")

answer = input("What symbol is commonly used to denote decorators in Python? ")
if answer == "@":
    print('Correct!')
    score += 1
else :
    print("Incorrect!")

answer = input("Is a class method associated with the instance or the class itself? ")
if answer == "class":
    print('Correct!')
    score += 1
else :
    print("Incorrect!")

answer = input("What is the primary purpose of using lambda functions in Python? ")
if answer == "anonymous":
    print('Correct!')
    score += 1
else :
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score /4) * 100) + "%")
