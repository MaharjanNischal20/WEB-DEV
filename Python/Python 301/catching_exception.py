num1 = input("Enter first number")
num2 = input("Enter second number")

try:
    num1 = int(num1)
    num2 = int(num2)
    div = num1/num2

except  ValueError:
    print("Please enter the valid number.")
    div="Error"

except ZeroDivisionError:
    print("Number cannot be divided by zero")
    div="Error"

except Exception as e: #it gives the name of the error so that we can handle that exception 
    print("Exception was caught")
    print(type(e))
    div="Error"

print(div)