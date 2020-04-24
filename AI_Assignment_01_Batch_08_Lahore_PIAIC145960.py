#AI_Assignment_01
#Batch_08_Lahore
# Student_Registration_ID_PIAIC145960

#Probalm: We do need to take two number for user and have to do following operations on those
# 1-Multiplication 2-Division 3-Addtion 4 Subtration

first_number = 0
second_number = 0

welcome_message = "We have to do basic math operation please enter two numbers"

print(welcome_message)

first_number = int(input("Please Enter First Number : "))
second_number = int(input("Please Enter Second Number : "))
print(f"You have enter {first_number} as 1st number ")
print(f"You have enter {second_number} as 2nd number ")

multiplication_of_numbers = first_number * second_number
addition_of_numbers = first_number + second_number
subtraction_of_numbers = first_number - second_number
devision_of_numbers_1st_devide_2nd = first_number/second_number
devision_of_numbers_2nd_devide_1st = second_number/first_number

print(f"Multiplication of First Number: {first_number} with Second Number: {second_number} is = {multiplication_of_numbers}")
print(f"Addition of First Number: {first_number} with Second Number: {second_number} is = {addition_of_numbers}")
print(subtraction_of_numbers)
print(devision_of_numbers_1st_devide_2nd)
print(devision_of_numbers_2nd_devide_1st)