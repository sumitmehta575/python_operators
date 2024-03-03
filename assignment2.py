#1.Calculate the sum, difference, product, and quotient of two numbers.

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
sum = num1+num2
difference = num1 - num2
product = num1*num2
quotient = num1/num2

print("sum:",sum)
print("difference",difference)
print("product",product)
print("quotient",quotient)
print("hello")

#2.Perform various assignment operations on a variable.

x = 5
y=10
z=43
a=56
b=65
c=43
d=23
e=21

y += 2      #equivalent to y = y+2

z -= 2       #equivalent to z = z-2

a *= 2      #equivalent to a = a*2

b /= 2       #equivalent to b = b/2

c %= 2       #equivalent to c = c%2

d *=2      #equivalent to d = d*2

e //=2       #equivalent to e = e//2

print(a)
print(b)
print(c)
print(d)
print(e)
print(z)
print(y)
print(x)

#3.Compare two numbers and print the results.

a=5
b=10

if a>b:
    print("a is greater")
elif b>a:
    print("b is geater")
else:
    print("ais equal to b")

#4.Check conditions using logical operators.

num1=int(input("enter the value of num1 :"))
num2=int(input("enter the value of num2 :"))
num3=int(input("enter the value of num3 :"))

if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greater")
elif num3>num1 and num3>num2:
    print("num3 is greater")
else:
    print("any two number is equal")

#5.Check the identity of @ariable

a=35  # if the value of a and b is equal...
b=34
a is b

a=32    #if a is not equal to b...
b=54
a is b

#6.Perform bitwise operations on any two integers.

a = 32
b = 54
c = a&b
print(c)
bin(a)
bin(b)
bin(c)

#7.#Use unary operators to change the sign of a number.

a = 2  
b = -(a)
print("value of a : ", a)
print("value of b : ", b)

#8.Use the ternary operator to assign values based on conditions.

a=5
b=7
print(a,"is greater") if (a>b) else print(b,"is Greater")