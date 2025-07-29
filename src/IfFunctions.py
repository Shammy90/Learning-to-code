name = input("What is your name? ")
age = int(input(f"Hello, {name.title()}. How old are you? "))

if age  >= 18:
    college_degree = True
else:
    college_degree = False

if college_degree == True:
    print(f"Your name is {name.title()}. You are {age} and you do have a college degree")
else:
    print(f"Your name is {name.title()}. You are {age} and you do not have a college degree")



