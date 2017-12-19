def palindrome(j):
    rev = 0
    rem = 0
    temp = j
    while temp > 0:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp = temp // 10
    if rev == j:
        return True

def check(min,large) :
    max = 0
    for i in range(large-1, min, -1):
        for j in range(large - 1, min, -1):
            mul = i * j
            if palindrome(mul) == True:
                temp = mul
                if(temp>max) :
                    max=temp
                    break
    print(str(max) + "is the largest palindrome product")


if __name__ =="__main__" :
    check(100,998)






