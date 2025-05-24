"""1. After flipping a coin 10 times you got this result,
 result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads"""

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in range (len(result)):
    if result[i] == "heads":
        count+=1

print(count)

"""2. Print square of all numbers between 1 to 10 except even numbers"""
for i in range(10):
    if(i%2!=0):
       print(i*i)

''' 3. Your monthly expense list (from Jan to May) looks like this,
 expense_list = [2340, 2500, 2100, 3100, 2980]
 Write a program that asks you to enter an expense amount and program
 should tell you in which month that expense occurred. If expense is not
 found then it should print that as well.'''

expense_list = [2340, 2500, 2100, 3100, 2980]
month=["January","February","March","April","May"]
count=0
a=0
amount= int(input("Enter the amount of expense: "))
for i in range (len(expense_list)):
    if(amount == expense_list[i]):
       count=i
        
if(count==0):
    print("No expense")
else:
    print(f"It ocurred in month {month[count]}")

''' 4. Lets say you are running a 5 km race. Write a program that,
    i. Upon completing each 1 km asks you "are you tired?"
    ii. If you reply "yes" then it should break and print "you didn't finish the race"
    iii. If you reply "no" then it should continue and ask "are you tired" on every km
    iv. If you finish all 5 km then it should print congratulations message'''

for i in range(1,6):
    ans=input("Are you tired?")
    if(ans=="yes" and i<5):
        print("You didn't finish the race.")
        break
    elif(i==5):
        print("Congratulations! You finished the race.")
    else:
        continue


''' 5. Write a program that prints following shape
 *
 **
 ***
 ****
*****'''


for i in range(1,6):
    print(i*"*")


  
