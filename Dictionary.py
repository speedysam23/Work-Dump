cities = {"nepal":"Kathmandu", "italy": "Rome", "england": "London", "france":"Paris", "germany":"Berlin","japan":"Tokyo"}
x=1
while x == 1:
    x=0
    CountryChoice = input("Please enter the name of a country:")
    CountryChoice = CountryChoice.lower
    if (CountryChoice) in cities:
        print("Yes")
        x=1
    elif (CountryChoice) not in cities:
        print("No")
        x=1


