def mult():
    a,b = None, None
    while True:
        a, b = input("Enter Two Numbers to Multiply: ").split()
        try:
            a = float(a)
            b = float(b)
            break
        except TypeError:
            print("You did not enter two numbers")
    product = a * b
    print(f'The Product of {a} and {b} is {product}')
    

