print("Welcome to the Calculator")    
print("Please select the operators to you want!")
print("1 . Addition")
print("2 . Subraction")
print("3 . Multiplication")
print("4 . Division")

def add(x,y) :
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division (x , y):
    return x/y


while True:
    choice = input("Enter the choice (1/2/3/4):")
    
    if choice in('1' , '2' , '3' , '4'):
        try:
            num1 = float(input("Enter the firnt number :"))
            num2 = float(input("Enter the second number :"))

        except:
                print("Please enter the valid input!")

        
        if choice == '1' :
            print(num1  , '+' , num2 ,'=', add(num1,num2))

        elif choice =='2':
            print(num1 , '-' , num2 , '=' , sub(num1 , num2))
        elif choice == '3' :
            print(num1 , '*' , num2 , '=' , multiply(num1 , num2) )

        elif choice == '4':
            print(num1 , '/' , num2 , '=' , division(num1 , num2))


        next_calculation = input("Lets do the another calculation (Yes / No ) : ")
        if next_calculation == "no" :
            break

    else :
        print("Invalid input")

