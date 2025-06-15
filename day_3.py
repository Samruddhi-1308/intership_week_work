#1 to 10 numbers using while loop
i=1
while i<=10:
    print(i)
    i+=1


# # 1 to 10  using for loop
for i in range(1,11):
    print(i)


# even numbers 
num=int(input("enter numbers:"))
for i in range(1,num):
    if i%2==0:              #for odd number (i%2==1)
        print(i)


# table 
num = int(input("enter numbers:"))
for i in range(1,11):
    print(num ,"*",i,"=",num*i )


# addition of numbers
sum=0
for i in range (1,11):
    sum +=i
print(sum)


# factorial of numbers
num = int (input("enter number:"))
fact=1
for i in range (1,num+1):
    fact =fact*i
    print(fact)


# find prime number
num = int(input("enter number:"))
count=2
while count<=2:
    
    if num%count==0:
        break
    count +=1
print("counter:",count)

if(count==num):
    print("number is prime")
else:
    print("number is not prime")
