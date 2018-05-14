name = "Preston"

subjects = ["Math", "History", "Science"]


print ("My name is " + name)

for i in subjects:
    print ("I take " + i +" as one of my classes.")

goodfootballplayers = ["tom bradey", "Nick foles", "Crooks", "rob growkoski"]

for i in goodfootballplayers:
    if i == "tom bradey":
        print("tom bradey is the best")
    print (i + " was in the superbowl!")



books = []

while True:
    print("who is your favorite football player? type 'end' to stop")
    answer = input()
    if answer == "end":
        break
    books.append(answer)
    
for i in books:
    print (i + " is one of your favoirtes.")
