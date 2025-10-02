
#My calcilator

#start

number_1 = ""
number_2 = ""
operation_number = ""
result = ""

print("Hi, here is my calculator")

print("What you wont to do? " \
        "Addition - write 1" \
        "Subtraction - write 2" \
        "Multiplication - write 3" \
        "Division - write 4")

operation_number = input()
operation_number = int(operation_number)

print("Write first number")
number_1 = input()
number_1 = int(number_1)

print("Write second number")
number_2 = input()
number_2 = int(number_2)

def addition(number_1, number_2):
        result = number_1 + number_2

def subtraction(number_1, number_2):
        result = number_1 - number_2

def multiplication(number_1, number_2):
        result = number_1 * number_2

def division(number_1, number_2):
        result = number_1 / number_2

def what_operation(operation_number):
        if operation_number == 1:
            addition(number_1, number_2)
        
        if operation_number == 2:
            subtraction(number_1, number_2)

        if operation_number == 3:
            multiplication(number_1, number_2)

        if operation_number == 4:
            division(number_1, number_2)

what_operation(operation_number)

result = str(result)

print(result)