 """Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
i)Write a program that asks user to enter a city name and 
it should tell which country the city belongs to
ii)Write a program that asks user to enter two cities and it tells you if
they both are in same country or not. For example if I enter mumbai and chennai, 
it will print "Both cities are in India" but if I enter mumbai and dhaka it should print
"They don't belong to same country" """


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#1(i).
city=input("enter city:")
if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in Pakistan")
elif city in bangladesh:
    print(f"{city} is in Bangladesh")
else:
    print(f"I do not know where {city} is ")

#1(ii).
city1=input("Enter city no 1: ")
city2=input("Enter city no 2: ")

if(city1 in india and city2 in india):
    print(f"Both {city1} and {city2} are in India")
elif(city1 in pakistan and city2 in pakistan):
    print(f"Both cities {city1} and {city2} are in Pakistan")
elif(city1 in bangladesh and city2 in bangladesh):
    print(f"Both {city1} and {city2} are in Bangladesh")
else:
    print("They don't belong to same country")
