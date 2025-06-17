# simple function program
def add():
    num1 =int(input("enter number:"))
    num2 =int(input("enter number:"))
    res = num1 + num2

    print("result :",res)

add()


# digit separated 
def digit():
    
    num =int(input("enter number:"))
    rem =0

    while num>0:
        rem = num%10          # last digit display
        print(rem)
        num = int(num/10)       #last digit remove

digit()


# number is palindrom
def palindrome():
    num = int(input("enter number:"))
    rev =0
    temp =num

    while num>0:
        digit = num%10
        rev = rev*10 +digit
        num=num//10

    print(rev)

    if temp==rev:
        print("number is palindrome")
    else:
        print("number is not palindrome")

palindrome()


# armstrong number


# power calculation
def power():
    num = int (input("enter number:"))
    pow = int(input("enter number:"))
    sum=1

    while pow>0:
        sum*=num
        
        pow-=1
    print(sum)
power()        