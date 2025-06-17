# without parameter with return
def add():

    num1 = int(input("enter number:"))
    num2 = int(input("enter number:"))

    res =num1 + num2
    return res

print(add())
print(add()+10)


# check even odd number
def evenodd():
    num = float(input("enter number:"))
    
    if num%2==0:
        return "number is even"
    else:
        return "number is odd"
    
a= evenodd()
print(a)
print(type(a))


# with parameter without return

def add (num1, num2):
    
    result = num1 + num2
    print("result :", result)

add(10,20)



# net salary

def netsalary(bs, hra ,da ,pf):

    net_salary = bs + hra + da - pf
    print("net salary:",net_salary)

a =float(input("enter basic salary:"))
b =float(input("enter hra:"))
c =float(input("enter da:"))
d =float(input("enter pf:"))

netsalary(a,b,c,d)



# with parameter with return
def ns(ba,hra,da,pf):

    ns = ba + hra + da - pf
    return ns

n =ns(1000,2000,3000,2000)
print(n)



