# 7/28/2025

#  while loops run the codes until the condition is true.
# so basically, this runs until the condition is false. Makes sense

#count = 0
#
#while count <3:
#    print("Count is:", count)
#    count += 1

# question = int(input("What is 5 + 2 "))
# 
# while question != 7:
#     question = int(input("That is not correct, please try again "))
#     print("That is correct!")

# for loops repeats a known number of times.

# for i in range(0, 100, 1):
#   print(i)

# names = ["Alice", "Bob", "Charlie"]
# 
# for i, name in enumerate(names):
#     print(i, name)


# while True:
#     answer = input("Type 'quit': ")
#     if answer == "quit":
#         break
# 
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# 
# 
# for i in range(2):
#     for j in range(3):
#         print(f"i={i}, j={j}")
# 
# response = input("Yes or no? ").lower()
# while response not in ["yes", "no"]:
#     response = input("Invalid! Say yes or no: ").lower()
# print("Thanks for answering", response)
# 
# total = 0
# for i in range(1, 6):
#     total += i
# print("Total:", total)
# 
# while True:
#     choice = input("Choose (a/b/q): ").lower()
#     if choice == "q":
#         break
#     elif choice in ["a", "b"]:
#         print("Valid choice!")
#     else:
#         print("Invalid")


name = input("What is your name? ")
age = int(input(f"Hello, {name.title()}. How old are you? "))

while age not in range(1, 120):
    age = int(input("Invalid response. Please answer with a valid age. "))

print(f"Thank you for the information, {name.title()}.")

college_degree = input(f"Now, {name.title()}. Do you have a college degree? ").lower()

while college_degree not in ["yes", "no"]:
    college_degree = input("Not a valid response. Please answer with a yes or no. ")

print(f"Thank you, you answered {college_degree}.")

if age >= 18 and college_degree == "yes":
    print("Nice. You have a college degree.")
elif age < 18 and college_degree == "yes":
    print("I strongly doubt that.")
elif age >= 24 and college_degree == "no":
    print("Yea, college aint for everyone")
else:
    print("You are probably too young to have a college degree.")
       
