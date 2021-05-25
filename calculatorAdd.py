# adding two numbers 
def add():
    x,y = input("Enter two numbers to add: ").split()
    sum = int(x) + int(y)
    print('The sum of adding {0} and {1} is {2}'.format(x, y, sum))

add()