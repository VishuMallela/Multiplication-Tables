# Python program to find the multiplication table (from 1 to 10) of the entered number
#Project by VishuMallela

import time

#Intro
print("Welcome to tables.py by\nVishuMallela")
time.sleep(1)
print("Do check out my other projects!")
time.sleep(1)
print("Check out my profile\n@ github.com/VishuMallela")
time.sleep(1)
    
#Take input from user
i = 1
num = int(input("Enter the number whose multiplication table you want to be displayed: "))
time.sleep(1)
times = int(input("Enter the number till where you require the multiplication table: "))
time.sleep(1)

#Fix the loop

print("\nLoading the multiplication table of", num, "till", times)
time.sleep(3)

#Set the table

while i <= times:
   
   time.sleep(.3)
   
   print(num, "X", i, "=", num*i)

   i = i + 1

#Final credits

print("\nThank you for using this program!")
time.sleep(1)
print("More features coming soon, stay tuned!")
time.sleep(1)
print("Don't forget to check out my other projects!")
time.sleep(2)
print("Goodbye :)")
time.sleep(3)




   
