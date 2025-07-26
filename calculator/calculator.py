def add (n1, n2):
    return n1 + n2
def sub (n1, n2):
    return n1 - n2
def mul (n1, n2):
    return n1 * n2
def div (n1, n2):
    return n1 / n2
operations = {
    "+": add,  "-": sub,  "*": mul,  "/": div,
}
def calculator():
    art = """"   
             _____________________
            |  _________________  |
            | |  MY CALCULATOR  | |
            | |_________________| |
            |  ___ ___ ___   ___  |
            | | 7 | 8 | 9 | | + | |       
            | |___|___|___| |___| |    
            | | 4 | 5 | 6 | | - | |
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | |
            | |___|___|___| |___| |
            | | . | 0 | = | | / | |
            | |___|___|___| |___| |
            |_____________________|  

"""
    print(art)

    should_accumulate = True
    num1 = float(input("What is first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("What is the operation you want to do?: ")
        num2 = float(input("What is next number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()


