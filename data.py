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