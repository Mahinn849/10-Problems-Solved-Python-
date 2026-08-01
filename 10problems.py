# // -- (1) Interest Calculator -- //
# principal_amount = int(input("Enter Your Amount: "))
# rate_of_interest = float(input("Enter Interest: "))
# time = int(input("Enter Time (years): "))
# interest = (principal_amount * rate_of_interest * time) / 100
# total_amount = principal_amount + interest

# print(f"Amount: {principal_amount}")
# print(f"Simple Interest: {interest}")
# print(f"time: {time}")

# print(f"Your Total Final Amount: {total_amount}")

               # // -- (2) Even odd check -- //

# number = int(input("Enter a Number: "))
# remainder = number % 2




# if remainder == 0 and number > 0:
#     print("This is an even number and it's POSITIVE 1")

# elif remainder == 0 and number == 0:
#     print("This is an even number and it's ZERO 2")

# elif remainder == 0 and number < 0:
#     print("This is an even number and it's NEGATIVE 3")


# elif remainder != 0 and number > 0:
#     print("This is an odd number and it's POSITIVE 4")



# elif remainder != 0 and number < 0:
#     print("This is an odd number and it's NEGATIVE 6")


# else:
#     print("Please Enter an Integer")


     # // -- (3) Grade Calculator -- //
# 90-100: A
# 75-89: B
# 60-74: C
# 40-59: D
# Below 40: F

# marks = int(input("Please Enter your Marks: "))

# if marks >= 90:
#     print("Your Grade is A ")

# elif marks >= 75:
#     print("Your Grade is B ")

# elif marks >= 60:
#     print("Your Grade is c ")

# elif marks >= 40:
#     print("Your Grade is D ")

# elif marks < 40:
#     print("Your Grade is F ")





# // -- (4) TABLE using for loop -- //

# number = int(input("Please enter any number for make Table: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


# // -- (5) Sum of Digits -- //

# number = int(input("Please enter numbers: "))
# total = 0


# while number > 0:
#     digit = number % 10
#     total = total + digit
#     number = number // 10

# print(f"Sum of Digits: {total}")


# // -- (6) Reverse a Number  -- //




# number = int(input("Enter a Number: "))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit

#     number = number // 10

# print(f"Reverse Number: {reverse}")

        # // -- (7) Reverse a Number  -- //
# number = int(input("Enter a Number: "))

# is_prime = True

# if number <= 1:
#     print("It is not a Prime Number")

# else:
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("It is a Prime Number")

#     else:
#         print("It is not a Prime Number")


# // -- (8)  Sum of Natural Numbers for loop-- //



# number = int(input("Enter a Number: "))

# total = 0

# for i in range(1, number + 1):
#     total = total + i

# print(f"Sum of Natural Numbers (For Loop): {total}")

# # // -- (8)  Sum of Natural Numbers while loop -- //

# number = int(input("Enter a Number: "))

# total = 0
# count = 1

# while count <= number:
#     total = total + count
#     count = count + 1

# print(f"Sum of Natural Numbers (While Loop): {total}")




# // -- (9) Simple Calculator -- //
# num1 = float(input("Enter First Number: "))
# num2 = float(input("Enter Second Number: "))
# operator = input("Enter Operator (+, -, *, /): ")

# if operator == "+":
#     print(f"Answer: {num1 + num2}")
# elif operator == "-":
#     print(f"Answer: {num1 - num2}")
# elif operator == "*":
#     print(f"Answer: {num1 * num2}")

# elif operator == "/":
#     if num2 == 0:
#         print("Division by zero is not allowed")
#     else:  
#         print(f"Answer: {num1 / num2}")

# else:
#     print("Invalid Operator")

# // -- (10) Number Pattern Printing -- //


number = int(input("Enter a Number: "))

for i in range(1, number + 1):
    for j in range(i):
        print("*", end="")
    print()

