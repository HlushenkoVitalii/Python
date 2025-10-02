"""
This function take integer age as Argument and
print if he/she/they/them is old or will be old
"""


def ageMashine(age: int)->None:
        if age > 50:
            print("Du bist alt geworden!")
        else:
            print("Aha, eines Tages du wirst Alt auch!")



print("How old are you?")
#input function is always a string
#input function is something like async in javascript
# 
age_from_user = input()
age_from_user = int(age_from_user)

ageMashine(age_from_user)


        
"""
this function accept two integer as Argument and add them
return result of summation
"""


def addTwoNumber(first_number:int, second_number:int)->int:
     return first_number+second_number

result = addTwoNumber(5,6)
print(f"is is result: {result}")

