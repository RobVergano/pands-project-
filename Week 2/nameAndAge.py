#nameAndAge.py
#this program reads name and age
#author: Roberto Vergano

from more_itertools import difference


name = input ("Enter your name:")
years = input ("Enter your age:")
print ("Hello " + name +"," + "\tYour age is " + years + "\nNice to meet you")
newage = int(years) - 4
print (newage)