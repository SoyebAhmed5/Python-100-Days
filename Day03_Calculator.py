def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ZeroDivisionError("Cannot divide by 0")
    return x/y

def menu():
    print("_____Select the operation to perform_____")
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')



while True:
    menu()
    choice=int(input("Enter your Choice 1-5:"))
    
    if choice>0 and choice<6:
        
        if choice == 5:
            print("Exiting the operation")
            break
        
        try:
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))
            match choice:
                case 1:
                    print("Result:",add(num1,num2))
                case 2:
                    print("Result:",subtract(num1,num2))
                case 3:
                    print("Result:",multiply(num1,num2))
                case 4:
                    print("Result:",divide(num1,num2))
                case _:
                    print('Invalid choice')
                    
        except ValueError:
            print('Invalid input')
            
        except ZeroDivisionError as e:
            print(f'Error:{e}')
            
        except Exception as e:
            print('Unexpected Error occur')
            
        finally:
            print('Operation performed now restarting')
    else: 
        print(f"Invalid Choice")    
                        