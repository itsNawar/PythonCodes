"""
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21

Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their 
population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. If country 
already exist in our dataset then it should print that it exist and do nothing. 
If it doesn't then it asks for population and add that new country/population in 
our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist 
in our dictionary then remove it and print new dictionary using format shown above in (a).
Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. 
When user inputs that country it will print population of that country.
"""



country_list={"China":143,"India":136,"USA":32,"Pakistan":21}

def print_countries():
    for key in country_list:
        print(key,"==>",country_list[key])


def add (name):
    if(name in country_list):
        print("It exists!")
    else:
        population= int (input("Enter the population"))
        country_list[name]=population
        print(country_list)



def remove (name):
    if(name in country_list):
        del country_list[name]
        for key in country_list:
            print(key, "==>", country_list[key])
    else:
        print("It doesn't exists!")



def query(name):

    print(name,"==>",country_list[name])


ask=input("print,add or remove:")
if(ask=="print"):
    print_countries()
if(ask=="add"):
    name=input("Enter the country name")
    add(name)
if(ask=="remove"):
    name=input("Enter the country name")
    remove(name)

ask1=input("which country you want to query?")
query(ask1)






