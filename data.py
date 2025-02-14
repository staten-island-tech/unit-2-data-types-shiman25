""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[0])
print(values[6])
 """

""" "test"
["t","e","s","t"]

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" #input & save that input
#split that input
#count how many words

sentence = input("Type a sentence: ")
words = sentence.split( ) #
print(words)
number = len(y)
print("You typed in", number, "words")
print(number)

def count(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        count += 1
    return count
print(count(sentence)) """

""" def login(password):
    #if statement evaluates to true do next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect password")
    login("secret") """

""" def temp(x):
    if x >=80:
        print("too hot")
    elif x >60:
        print("nice")
    else:
        print("Too Cold")
x = int(input("what da the temp"))
temp(x) """

""" #booleans and Control Flow
day_of_the_week = input("what day is it? ")
if day_of_the_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" 
#F String
x = test
print(f"hello {x}")
temp = 75
if temp > 68:
    print('warm')
 """

""" #Challenge
number = int(input("Type in a integer! ")) #let user type in a num
if number%2 == 0: #if the remainder is 0 when divided by 2, is even
    print("The Number is Even! :) ") 
else: #if the remainder is anything else; which can only be 1
    print("The Number is Odd! :( ") """

#Challenge.2 
""" try:
    bill = float(input("What is your bill? "))
    service = input("How was your experience? (bad, okay, good, or great): ")
    if service == "bad":
        tips = 0
    elif service == "okay":
        tips = bill * 0.15
    elif service == "good":
        tips = bill * 0.2
    elif service == "great":
        tips = bill * 0.25
    
    print(f"Recommended tips: {round(tips,2)}")
except ValueError:  # This block runs if the user enters something
    print("Invalid. Please Try Again") 
 """
#Challenge.2 alt
try:
    bill = float(input("What is your bill? "))
except ValueError:
    print("Invalid. Please Try Again")
    exit()

service = input("How was your experience? (bad, okay, good, or great): ")
if service == "bad":
        tips = 0
elif service == "okay":
        tips = bill * 0.15
elif service == "good":
        tips = bill * 0.2
elif service == "great":
        tips = bill * 0.25  
else:
    print("Invalid. Please Try Again") 
    exit()

print(f"Recommended tips: {round(tips,2)}")

#challenge.3

#use modulo to check remainder for 1 factor
#use a loop to check all potential factors range(2,15)
#conditional statement if factor append to list

""" def find_factors(number): #define the finding of the number
    x = [1] #starting the list of 1
    for i in range(2, number): #i is the number in the range between 2 and number-1
        if number % i == 0: #if number divided by i evenly
            x.append(i) #put it in the factors list    
    x.append(number) #the number is always factors of itself
    return(x)
number = int(input("Type a number: ")) #type a number
factors = find_factors(number) #find the factors of a number
print(factors) """


""" isRich = True
is21 = True
def canGamble(isRich, is21):
    if isRich == True and is21 == True:
        print("Let it ride!")
    elif isRich == False and is21 == True:
        print("your too poor!")
    elif isRich == False or is21 == False:
        print("you cannot play") """

#LastChallenge
#set x and y as the 2 numbers
#find factors of BOTH at the same time
#if find then stop.
#print that number
""" x = int(input("Type in a whole number: "))
y = int(input("Type in another whole number: "))

def find(num1,num2): #comparing 2 nums
    if num1 > num2: 
        good = num1
        return(good)
    else:
        good = num2
        return(good)
good = find(x,y)

def gcf(num1,num2): #Finding the gcf of 2 numbers
    factors = [1] #the list of common factors
    trash = [1] #the list of numbers that does not meet the requirement
    for i in range(2,good): #loop from 2 to num2?
        if num1%i != 0 or num2%i != 0: #if the number i is not one or both factor
            trash.append(i) #move to trash
        elif num1%i == 0 and num2%i == 0: #if number i is both numbers' factor
            factors.append(i) #sent it to factors list
            
    print(factors[-1]) #print the last number of the factors list

GreatestCommonFactor = gcf(x,y) """
###############################################################################
""" x = int(input("Type in a whole number: "))
y = int(input("Type in another whole number: "))

def gcf(num1,num2): #Finding the gcf of 2 numbers       
  
    if num1 < num2: 
        smaller = num1
    else:
        smaller = num2
        
    for i in range(smaller, 0 , -1): #loop from the smaller num backwards
        if num1%i == 0 and num2%i == 0: #if the number i is both factor
            print(i)
            return(i)
GreatestCommonFactor = gcf(x,y) """