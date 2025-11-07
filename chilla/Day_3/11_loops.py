# This python script is about loops in python
 
# # while loop
# i = 1
# while i < 5:
#     print("i is:", i)
#     i += 1  # Increment i by 1

# # for loop
# for j in range(5,10):
#     print("j is:", j)   


# loop with array
fruits = ["apple", "banana", "cherry", "mango", "orange"]
for fruit in fruits:
    if fruit == "banana": continue
    if fruit == "mango": break
    print("fruit is:", fruit)