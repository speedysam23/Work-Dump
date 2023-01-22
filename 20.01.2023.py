#                              OUTPUTS, INPUTS AND VARIABLES



#Question 1
#favcolour = str(input("What is your favourite colour?"))
#print ("Your favourite colour is", favcolour)

#Question 2
fn = str(input("What is your first name?"))
mnDec = str(input("Do you hav multiple middle names?"))
mnDec = mnDec.lower
if mnDec == ("yes"):
    mn = str(input("What are your middle names?"))
else:
    mn = str(input("What is your middle name?"))
ln = str(input("What is your last name?"))

print ("Your name is",fn,mn,ln)




















#                              CASTING, RANDOM NUMBERS AND MATHS

#Question 1

# num = int(input("Enter a number"))
#print(num*num)



#Question 2

#allowance = int(input("How much pocket money do you get a week?"))
#phonespend = int(input("How much did you spend on your phone this week?"))
#snackspend = int(input("How much money did you spend on snacks this week?"))
#moneyleft = allowance - phonespend - snackspend
#print ("You have", moneyleft, "pounds left")



#Question 3

#import random
#x = 1
#rangelow = int(input("Enter the first number"))
#while x == 1:
#    x = 0
#    rangehigh = int(input("Enter the second number"))
#    if rangehigh<rangelow:
#        print ("Please enter a number greater than",rangelow)
#        x = 1
#    else:
#        print (random.randint(rangelow,rangehigh))
