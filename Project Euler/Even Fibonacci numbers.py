#The sum of the even-valued terms

first = 0
second = 1
fib = 0
sum = 0

while fib <= 4000000:

        fib = first + second
        first = second
        second = fib

if fib % 2 == 0:
    sum += fib


print(sum)

