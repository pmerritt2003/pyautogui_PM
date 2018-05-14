import time

subjects = {'English', 'French', 'Science', 'Math'}

for i in subjects:
    print ("One of my subjects is " + i)

foods = {'Wonton soup', 'ice cream', 'chicken soup',}

for i in foods:
    if i == "chicken soup":
        print("My favorite food is " + i + "!")
    else:
            print("I like to eat " + i )


friends = {'me', 'a snail i found in the ground', 'juan', 'king philip', 'tucker',}
for i in friends:
    print(i.title() + "is LIT")

myname = ""
letters = ['b','o','b',' ','t','h','e',' ','q','u','e','e','n']

for i in letters:
    myname = myname + i
    print(myname)
    time.sleep(0.5)
print (myname.title())
    

