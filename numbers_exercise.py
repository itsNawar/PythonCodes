# Exercise
#1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
long=92
wide=48.8
area=long*wide
print(area) # Ans: 4489.599999999999

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
each=1.49
spent=each*9
gave=20
back=gave-spent
print(back) # Ans: 6.59

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
side=5.5
cost_perfeet=500
area=side**2
cost=area*cost_perfeet
print(cost) # Ans: 15125.0

# 4. Print binary representation of number 17
num=17
print(format(num,'b')) # Ans: 10001
