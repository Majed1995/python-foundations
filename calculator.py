first = input("Enter the first number: ")

if not first.isdigit():
    print("The number is invalid")
    first = input("Enter the first number: ")
second = input("Enter the second number: ")
if not second.isdigit():
     print("The number is invalid")
     second = input("Enter the Second number:" )

operation = input("Choose the operation (+, -, /, *): ")    

if operation == "+":
    answer = int(first)+int(second)
elif operation == "-":
    answer = int(first)-int(second)
elif operation == "*":
     answer = int(first)*int(second)
elif operation == "/": 
     answer = int(first)/int(second)
else:
    answer = print("Invalid Entry")


print("The answer is %s"%(answer)) 
