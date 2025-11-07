# This python script is about conditional logics in python programming language
# types of logical operators
# equal to    ==
# not equal to !=
# greater than > 
# less than    <
# greater than or equal to >=   
# less than or equal to    <=
# and 
# or
# not
# True
#false

# application of logical operators
# age = 18
# age_at_school = 5
# print(age == age_at_school)  


# input function with conditional logics

age = int(input("What is Ali's age? "))
minimum_age_at_school = 5
max_age_at_school = 20
if age>= minimum_age_at_school and age<= max_age_at_school:
    print("Ali can attend school")

elif age>= max_age_at_school:
    print("Ali is too old to attend school")
else:
    print("Ali cannot attend school")