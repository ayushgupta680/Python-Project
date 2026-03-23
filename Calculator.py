def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide"
    return a / b

while True:
    print("\n Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = int(input("Enter choice:"))
    
    if choice == 5:
        print("Exit")
        break
    
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    
    if choice == 1:
        print("Result:", add(a,b))
    elif choice == 2:
        print("Result:", subtract(a,b))
    elif choice == 3:
        print("Result:", multiply(a,b))
    elif choice == 4:
        print("Result:", divide(a,b))
    else:
        print("Exit")