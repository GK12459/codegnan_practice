import calculator_back

operator_list  = ['+', '-', '*', '/', '%', '^']
while(True):
    print("\n---------CALCULATOR---------")
    print("\nOperations and Operators:\nAddition (+)\nSubtraction (-)\nMultiplication (*)\nDivision (/)\nReminder (%)\nExponent(^)\nExit (e)")
    operator = input("\nEnter operator: ")
    if(operator.lower() == "e"):
        print("\nThankyou for using calculator!")
        break
    if(operator not in operator_list):
        print("\nInvalid Operator!")
        continue

    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    match(operator):
        case '+':
            print("\nOperation__Addition")
            print(calculator_back.sum_(n1, n2))
        case '-':
            print("\nOperation__Subtraction")
            print(calculator_back.difference_(n1, n2))

        case '*':
            print("\nOperation__Multiplication")
            print(calculator_back.product_(n1, n2))

        case '/':
            print("\nOperation__Divission")
            print(calculator_back.quotient_(n1, n2))

        case '%':
            print("\nOperation__Remainder")
            print(calculator_back.modulus_(n1, n2))

        case '^':
            print("\nOperation__Exponent")
            print(calculator_back.exponent_(n1, n2))
        
    try:
        input('Click enter to continue')
    except:
        pass