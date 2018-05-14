import pyautogui as pg
import time
import webbrowser 
points = 0

answer = pg.prompt(
"""
How would you like to get around?

a)biking  
b)biking 
c)flying 


"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+=3

    answer = pg.prompt(
"""
What is your ideal weapon?


a)slingshot 
b)My fists
c)my powers 


"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+=3

    answer = pg.prompt(
"""
What applies to you?

a)1 siblings 
b)only child
c)orphan  


"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+=3



answer = pg.prompt(
"""
If you had one wish what would it be?

a)more wishes 
b)Dart didn't eat things
c)never ending supply of waffles 


"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points+=3

    
    
#END OF SURVEY
    pg.alert("you are...")
    webbrowser.open ("https://cdn.pastemagazine.com/www/system/images/photo_albums/stranger-things-memes/large/stranger-things-33.gif?1384968217")
#lucas
if points < 6:
    ("Lucas")
#Dustin
if points  >=7 and points <9:
    pg.alert("Dustin")
    webbroswer.open ("https://img.buzzfeed.com/buzzfeed-static/static/2016-09/5/6/asset/buzzfeed-prod-fastlane03/sub-buzz-24184-1473070157-19.png?downsize=715:*&output-format=auto&output-quality=auto")
#Eleven
if points >9 and points >=12:
    pg.alert ("Eleven")
    webbroswer.open ("https://78.media.tumblr.com/529cf0f4a99d63f050c66445e43cfdb4/tumblr_ob10d1hYxz1vsmrbvo1_1280.jpg")

    
