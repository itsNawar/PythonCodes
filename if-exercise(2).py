""" Exercise: Python If Condition
 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
     i. Ask user to enter his fasting sugar level
     ii. If it is below 80 to 100 range then print that sugar is low
     iii. If it is above 100 then print that it is high otherwise print that it is normal"""

#2(i)
sugar_level=int(input("Enter sugar level: "))

#2(ii)

if(sugar_level<80 ):
    print("Sugar is low")
#2(iii)
elif(sugar_level>100):
    print("Sugar is high")
else:
    print("Sugar is normal")



