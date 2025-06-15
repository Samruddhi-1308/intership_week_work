#first progarm
num1=int(input("enter number:"))
num2=float(input("enter number:"))

print(type(num1))
print(type(num2))

res = num1 + num2

print("result ="+str(res))



#doller and rupees
doll = int(input("enter doller:"))
rup = doll*85
print("doller to rupees:",rup)

rup2=int(input("enter rupees:"))
doll2=rup2/85
print("rupees to doller:",doll2)



#find area
radius = int(input("enter radius:"))
area_1=3.14*radius*radius
print("area of circle:"+str(area_1))


len=int(input("enter length:"))
breadth=int(input("enter breadth:"))
print("area of rectangle:",len*breadth)


side=int (input("enter side:"))
print("area of square:",side**2)


#find net salary
basic_salary = float(input("enter basic salary:"))
hra = float(input("enter HRA:"))
da = float(input("enter dA:"))
pf = float(input("enter PF:"))

net_salary = basic_salary + hra + da - pf

print("net salary ="+str(net_salary))

