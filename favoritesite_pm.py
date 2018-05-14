import webbrowser
import pyautogui as pg


videos = ["https://www.youtube.com/watch?v=KNRs_ZBMyD8","https://www.youtube.com/watch?v=nxyoZhIJIpw"]

music = ["https://www.youtube.com/watch?v=wZv62ShoStY","https://www.youtube.com/watch?v=eYJCjVkOImU"]


answer = pg.prompt (
"""
What do you want to do?
a) music
b) videos

"""
)


        
if answer == "a":
    for i in music:
        webbrowser.open(i)

elif answer == "b":
    for i in videos:
        webbrowser.open(i)
