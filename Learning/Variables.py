#Case sensitivity and rules to define varibles is explained
Greeting = "Crap"
greeting = "shit"
_greeting = "Holy mother fucking"

print(_greeting + greeting + Greeting)

#Printing different types together
TheNumber = 15
another = 4
print(TheNumber + another)
print(TheNumber - another)
print(TheNumber * another)
print(TheNumber / another)
print(TheNumber // another)
print(TheNumber % another)
print(TheNumber ** another)
print(TheNumber + another / 3 - 4 * TheNumber) #BODMAS


#print(Greeting+TheNumber) #Throws an error

parrot = "Norwegian Blue"
print(parrot[3]) #Prints the said index only
print(parrot[0:2]) #Prints from 0 and prints 2 characters
print(parrot[:4]) #Prints From start and prints 4 characters
print(parrot[2:]) #Prints from 2 and prints till the end
print(parrot[-4:- 2]) #Prints backwards
print(parrot[0:6:2]) #Prints from 0 and prints 6 elements and skips 2 elements in between

number = "9,223,372,036"
print(number[1::4])
numbers = "1, 2, 3, 4, 5"
print(numbers[0::3])


#String operators

string1 = "Deadpool"
string2 = " is awesome"
print(string1 + string2)

print("Alright " * 3) #Prints the original string 3 times

#Substring search
today = "Crapday"
print("day" in today) #Returns boolean