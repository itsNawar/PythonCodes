# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expenses=[2200,2350,2600,2130,2190]
#1.
extra_spent_in_feb=monthly_expenses[1]-monthly_expenses[0]
print(extra_spent_in_feb)

#2.
total_expense_in_three=monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]
print(total_expense_in_three)

#3.
a="2000" in monthly_expenses
print(a)

#4.
monthly_expenses.append(1980)
print(monthly_expenses)

#5.
refund=200
monthly_expenses[3]=monthly_expenses[3]-refund
print(monthly_expenses)




# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append("Black Panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove("Black Panther")
heros.insert(3,"Black Panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=["doctor strange"]
print(heros)    
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)
