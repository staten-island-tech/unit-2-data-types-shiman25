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

print(f"Recommended tips: {round(tips,2)}")
