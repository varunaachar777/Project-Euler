#String in Depth

age = 24
#str()
print("My age is " + str(age)) #str () converts the bracketed value to a string

#Replacement Fields

print("My age is {0} years" . format(age)) #the value in the format() field goes in to the numbered curly braces field
print("Some players with jersey number {0} are {1}, {2}, {3}".format(7, "Ronaldo", "Beckham", "Figo"))

#using the same replacement fields multiple times

print("""January : {2}
Frebruary: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

print("{0:4} shit is getting {1:8}spacious".format("Crap","Weasel"))
print("{0:4} shit is getting {1:<8}spacious".format("Crap","Weasel"))
#String Formatting Operator
print("My age is %d years" % age)
print("My age is %d %s, %d %s" %(age, "years", 6, "Months"))

for i in range(1,12):
    print("Number %2d squared id %4d and cubed is %4d" %(i, i ** 2, i ** 3 )) # %2d allocates 2 spaces to the variable and keeps it blank if the spaces aren't in use

print("pi is approximately %12.50f" % (22 / 7))
