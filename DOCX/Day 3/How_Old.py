# start

name = ""
year = ""
age = ""
actual_year = 2025


print("What is your name?")
name = input()

print("What is your year of birth?")
year = input()
year = int(year)

age = actual_year - year
age = str(age)

print("Cool, " +name+ ", your are "+age+" years old.")