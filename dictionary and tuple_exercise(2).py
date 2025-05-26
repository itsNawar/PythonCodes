"""You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. 
If stock already exist in your list (like info, ril etc) then it will append the
price to the list. Otherwise it will create new entry in your dictionary. 
For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks."""


stock={
    'info':[600,630,620],
    'ril': [1430,1490,1567],
    'mtl':[234,180,160]
}
def print_all():
    for item in stock:
        avg=round((stock[item][0]+stock[item][1]+stock[item][2])/3,2)
        print(item,"==>",stock[item],"==> avg:",avg)

def add (name,price):
    if(name in stock):
        stock[name].append(price)
    else:
        stock[name] = [price]
    for item in stock:

        print(item, "==>", stock[item])

task=input("print or add?")
if task=="add":
    name=input("enter stock ticker:")
    price=int(input("enter price:"))
    add(name,price)
if(task=="print"):
    print_all()

