first = 0
second = 1
fib = first + second
even_sum = 0

while fib <= 4000000:
    fib = first + second
    first = second
    second = fib
    if fib % 2 == 0:
        even_sum += fib

print(even_sum)