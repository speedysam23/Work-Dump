#def fact():
#    fact = 1
#    num = int(input("Enter a number"))
#    for i in range(1,num+1):
#        fact = fact * i
#     print ("The factorial of",num, "is", fact)
#fact()

for Counter in range(1,101,1):
    if Counter % 5 == 0 and Counter %3 != 0:
        print("Buzz")
    if Counter % 3 == 0 and Counter %5 != 0:
        print ("Fizz")
    if Counter %5 == 0 and Counter % 3 == 0:
        print("FizzBuzz")
    elif Counter %5 != 0 and Counter % 3 != 0:
        print (Counter)