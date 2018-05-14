import random

words = ["tiger","waterfalls","submarine","leaf","monkey"]
hint1 = ["orange","wet","water","trees","jungle"]
hint2 = ["rawr","fall","we all live in a yellow","fall during fall","ooh ohh ahh ahh"]

number = random.randint(0,4)
secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'length' 'first letter', 'last letter', or 'give up' if you need help.")
    guess = input()
    counter += 1

    if guess == secretword:
        print("you win")
        print("It took you " + str(counter) + " guesses.")
        break
        
    elif guess == "hint1":
        print(hint1[number])


    elif guess == "hint2":
        print(hint2[number])

    elif guess == "length":
        print( len(secretword) )


    elif guess == "first letter":
        print ( secretword[[0] )


    elif guess == "last letter":
        print( secretword[-1] )


    elif guess == "give up":
        print("It was  " + secretword)

    else:
        print("try again.")
        counter += 1
            

    
