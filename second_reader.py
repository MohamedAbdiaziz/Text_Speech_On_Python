import time
import pyttsx3
import socket

hostname = socket.gethostname()
print(hostname)


day = time.strftime('%A %d %B %Y')
text = f"""Assalamu Alaykum Guys!,
My name is Mohamed Abdulaziz,
Today i wanna teach you the subject of management specially chapter one.
The date of today is {day}. 
Lets start..............................................................
This chapter is named Managers and you in the workplace.
The first, we went to know who is the manager,
the second, Levels of management,
and the finally, what is their responsibility.
the first the manager is someone a coordinating and oversees the work of other people.
another wise manager is a person how manage what you do and gives instructions to work.
the second the levels of management are :
A. Top manager,
B. Middle manager,
C. First line manager, and
D. Non managerial employee.
these are necessary in every place like Companies, Schools, Universities and so on!
the finally their responsibility is making organization wide decision and establishing 
plans and goals and that effect the entire like income, profits.
if the company lose or success all of then effects the top manager.
this is the why the managers are important in organizations.
organizations needs their managerial skills and abilities now more than ever.
this concept is the main concept of this chapter, 
to get more information about this chapter go to the book please read.
that is it see you later. 
"""
print(text)

engine = pyttsx3.init()
engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.say(text)
engine.runAndWait()
engine.save_to_file(text, f"C:\\Users\\{hostname}\\Music\\chapter1.mp3")
engine.runAndWait()



