# Python program to find the multiplication table (from desired start to stop) of the entered number
#Project by VishuMallela

import time

#Intro
print("Welcome to tables.py Version 1.1 by\nVishuMallela")
time.sleep(1)
print("\nWe prefer you running this project in FULL SCREEN as it takes a lot of space.")
time.sleep(2)
print("\nWe've had a massive update recently.\nNow, you can choose the multiple where you want to start and stop the table!")
time.sleep(3)
    
#Take input from user
num = int(input("\nEnter the number whose multiplication table you want to be displayed: "))
time.sleep(1)
tablestart = int(input("Enter the multiple of the number from where you want to start the table: "))
time.sleep(1)
tablestop = int(input("Enter the multiple of the number from where you want to stop the table: "))
count = tablestart
time.sleep(1)

#Fix the loop

print("\nLoading the multiplication table of", num, "from", tablestart, "till", tablestop)
time.sleep(1)
print("\n")
time.sleep(1)

#Set the table

while count <= tablestop:
   
   time.sleep(.3)
   
   print(num, "x", count, "=", num*count)

   count += 1

#Final credits

print("\nThank you for using this program!")
time.sleep(1)
print("\nMore features coming soon, stay tuned!")
time.sleep(1)
print("\nDo check out my other projects!")
time.sleep(1)
print("\nCheck out my profile\n@ github.com/VishuMallela")
time.sleep(2)
print("\nGoodbye :)")
time.sleep(3)
