import math

#functions below
def add(a,b):
     result = a +b
     return result 


#main code below

print("This calculator allows you to add, subtract, multiply, or divide 2 numbers.")
a = input("Enter the first number: ")
while not a.isdigit():
    a = input("Invalid input. Please try again: ")
a = int(a)
    
b = input("Enter the second number: ")
while not b.isdigit():
    a = input("Invalid input. Please try again: ")
b = int(b)
    
oper = input("Enter the operation code (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")
while (not oper.isdigit()) or int(oper) < 1 or int(oper) > 4:
    oper = input("Invalid input. Please try again: ")
oper = int(oper)

if oper == 1:
    print(add(a, b))
elif oper == 2:
    print(subtract(a, b))
elif oper == 3:
    print(multiply(a, b))
elif oper == 4:
    print(divide(a, b))

    
#end of code