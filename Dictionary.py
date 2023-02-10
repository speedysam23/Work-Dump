cities = {"Nepal":"Kathmandu", "Italy": "Rome", "England": "London", "France":"Paris", "Germany":"Berlin","Japan":"Tokyo"}
x=1
while x == 1:
    x=0
    CountryChoice = input("Please enter the name of a country:")
    if (CountryChoice) in cities:
     print("Yes")
    elif (CountryChoice) not in cities:
       print("No")

