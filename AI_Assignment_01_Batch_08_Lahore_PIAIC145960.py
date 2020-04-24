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
subtraction_first_numbers_from_second = second_number - second_number
subtraction_second_numbers_from_first = first_number - second_number

print(f"Multiplication of First Number: {first_number} with Second Number: {second_number} is = {multiplication_of_numbers}")
print(f"Addition of First Number: {first_number} with Second Number: {second_number} is = {addition_of_numbers}")
print(f"Subtraction of First Number :{first_number} from Second Number :{second_number} is = ",subtraction_first_numbers_from_second)
print(f"Subtraction of Second Number :{second_number} from First Number :{first_number} is = ",subtraction_second_numbers_from_first)

if (first_number != 0) and (second_number != 0):
    devide_1st_by_2nd = first_number/second_number
    devide_2nd_by_1st = second_number/first_number
    print(f"Devide First Number :{first_number} by Second Number :{second_number} is =",devide_1st_by_2nd )
    print(f"Devide Second Number :{second_number} by First Number :{first_number}is =", devide_2nd_by_1st )
else:
    print("Any of entered number is 0 Zero so we cannot divide any number by Zero or if we devide zero by any number it will also ZERO ")
