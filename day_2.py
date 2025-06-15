#example 1
year= int (input("enter the year:"))
if year>=18:
    print("user is eligiable for voating")
else:
    print("user is not eligable for voating")


#example 2
per=int(input("enter percentage:"))
if per>=40:
    print("student pass")
else:
    print("student fail")


# example 3
num=int (input ("enter number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")


# example 4
year=int(input("enter year:"))
if year%4==0:
    print("year is leap")
else:
    print("year is not leap")


# example 5
num1=int(input("enter number:"))
num2=int(input("enter number:"))

if num1>num2:
    print("num1 is max")
else:
    print("num2 is max")


# example 6
num=int(input("enter number:"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")


# example 7
mark=int(input("enter marks:"))
if mark >=80:
    print("grade A")
elif mark >=60:
    print("grade B")
elif mark >=40:
    print("grade C")
else:
    print("fail")


# example 8
num1 = int(input("enter number:"))
num2 = int(input("enter number:"))
num3 = int(input("enter number:"))

if num1>num2 and num1>num3:
    print("num1 is max")

elif num2>num1 and num2>num3:
    print("num2 is max")

else:
    print("num3 is max")


# example 9
num1 = int(input("enter number:"))
num2 = int(input("enter number:"))
num3 = int(input("enter number:"))

if num1>num2:
    if num1>num3:
        print("num1 is max")
    else:
        print("num3 is max")
        
else:
    if num2>num3:
        print("num2 is max")
    else:
        print("num3 is max")

