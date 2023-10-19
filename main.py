#1
import random
dice = int(input("How many dice do you want to roll?: "))
sum = 0
for dice in range(dice):
    sideup = random.randint(1,6)
    sum += sideup
print(f"Sum of the numbers: {sum}")

#2

numbers = []
MAX_INPUTS = 5
for user_input in range(MAX_INPUTS):
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
        print("Quiz ended.")
    numbers.append(float(user_input))
if not numbers:
    print("No numbers were entered.")
else:
    numbers.sort(reverse=True)
    print("The five greatest numbers in descending order are:")
    for i in numbers:
        print(f"{i}")

#3
number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    number_type = "prime"
    if number <= 1:
        number_type = "not prime"
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                break
    print(f"{number} is {number_type}.")
else:
    print("Please enter a valid number.")

#4

city_list = []
for i in range(5):
    city_name = input(f"Enter the name of city {i + 1}: ")
    city_list.append(city_name)
print("City names:")
for i in city_list:
    print(i)








