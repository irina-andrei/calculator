# A calculator application that gives user 2 choices:
#   1. Calculating an equation they entered and saving to file.
#   2. Calculate all equations from a '.txt' file the user chooses.


def getting_values():
    """ A function validates the values received from user.
    Parameters: None
    Returns: float: 2 valid numbers, str: the operator """
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Oops! Remember we need valid numbers. Let's try again...")
    # The while loop will only break once both numbers entered are valid.
    
    operations = ['+', '-', '/', 'x']
    # The only valid operations saved as a list.
    
    while True:
        op = input("Enter the operation you want to perform (+ - / x): ")
        if op == '*':
            op = 'x'
        # As some users might enter '*' by mistake, we can easily fix that.
        
        try:
            if op not in operations:
                raise Exception(f"'{op}' is not a valid operator.")
        except Exception as error:
            print(f"{error} Let's try again.")
            continue
        # It will keep looping until user enters a valid operator.
        return num1, num2, op


def calculate(nr1, nr2, operator):
    """ A function that calculates an equation and checks for errors.
    Parameters: nr1(float), nr2(float), operator(str)
    Returns: int: solution or float: round(solution, 2) or str: 'Error' """
    
    try:
        if operator == '+':
            solution = nr1 + nr2
        elif operator == '-':
            solution = nr1 - nr2
        elif operator == 'x':
            solution = nr1*nr2
        elif operator == '/':
            solution = nr1/nr2
        
        if solution == int(solution):
            return int(solution)
        else:
            return round(solution, 2)
        # A user-friendly format (i.e. a rounded float or 4 instead of 4.0).
    
    except ZeroDivisionError:
        print("You can't divide by 0:")
        return "Error"
    except ValueError:
        print("This is not a valid entry:")
        return "Error"


def getting_file_name():
    """ A function that validates the file name from user.
    Parameters: None
    Returns: str: a valid and existing file name """
    
    while True:
        my_file = None
        try:
            filename = input("\nEnter filename: ")
            if filename.split('.')[1] != 'txt':
                print("Checking...")
            # This will check if user entered the filename with '.txt' or not.
            # If not, it will trigger the except block with an 'IndexError'.
        except IndexError:
            filename += '.txt'
            print("'.txt' was missing. I have added that for you.")
            print(f"Trying to find '{filename}'...")
        
        try:
            my_file = open(filename, 'r', encoding='utf-8')
            print(f"Success, we found '{filename}'.\n")
        except FileNotFoundError:
            print(f"Looks like '{filename}' does not exist. Let's try again.")
        
        finally:
            if my_file is not None:
                my_file.close()
                # If the file was successfully found, it needs to be closed.
            else:
                continue
        # The loop will keep looping until it receives a valid file name.
        return filename


valid_choices = ['1', '2', '3']

while True:
    print('''\nWhat would you like to do?
    1. Enter an operation to be solved.
    2. Solve a list of operations from a text file.
    3. Exit''')
    
    try:
        choice = input("Your selection: ")
        if choice not in valid_choices:
            raise Exception(f"Oops! '{choice}' is not a valid option.")
    
    except Exception as error:
        print(f"{error} You can only choose 1, 2 or 3. Let's try again.")
        continue
        # The while loop will keep looping until user enters 1, 2 or 3.
    
    if choice == '1':
        number1, number2, operation = getting_values()
        answer = calculate(number1, number2, operation)
        # Gets the values and calculates the answer for the equation.
        
        if answer == "Error":
            print(f"{number1} {operation} {number2} results in Error.")
        else:
            if number1 == int(number1):
                number1 = int(number1)
            if number2 == int(number2):
                number2 = int(number2)
            # # A user-friendly format (i.e. 7 instead of 7.0)
            
            answer = f"{number1} {operation} {number2} = {answer}"
            print(f"Answer: {answer}")
            with open('equations.txt', 'a', encoding='utf-8') as file:
                file.write(answer + "\n")
                print("Equation was saved to 'equations.txt'.")
            # Printing the answer as well as saving it to 'equations' file.
    
    elif choice == '2':
        file_name = getting_file_name()
        file = open(file_name, 'r', encoding='utf-8')
        
        print("Solutions:")
        for line in file:
            number1, operation, number2 = line.strip().split(" ")
            number1 = float(number1)
            number2 = float(number2)
            answer = calculate(number1, number2, operation)
            # For each line, getting the equation from file and calculating.
            # Assuming the format in the file for each line is <'A' 'op' 'B'>
            
            if number1 == int(number1):
                number1 = int(number1)
            if number2 == int(number2):
                number2 = int(number2)
            # # A user-friendly format (i.e. 7 instead of 7.0)
            
            if answer == "Error":
                print(f"{number1} {operation} {number2} results in an Error.")
            else:
                print(f"{number1} {operation} {number2} = {answer}")
            # If there were no errors, prints final result.
        
        file.close()
    
    elif choice == '3':
        print("Goodbye.")
        break