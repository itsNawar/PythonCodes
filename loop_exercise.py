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




  
