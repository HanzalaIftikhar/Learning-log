#this python script is about if, else and elif statements in python programming language

age = int(input("What is Ali's age? "))
minimum_age_at_school = 5
max_age_at_school = 20
if age>= minimum_age_at_school and age<= max_age_at_school:
    print("Ali can attend school")

elif age>= max_age_at_school:
    print("Ali is too old to attend school")
else:
    print("Ali cannot attend school")