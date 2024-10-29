while True:
    try:
        x = int(input("Enter the value of x : "))
    except ValueError:
        print("Entered value of x is not an integer!!")
    else:
        break
print(f"x is {x}")
#We Could Also Do :
#while True:
#     try:
#         x = int(input("Enter the value of x : "))     Here if we catch the ValueError
#         break                                         exception it will jump on except block without
#                                                       executing the break statement
#     except ValueError:
#         print("Entered value of x is not an integer!!")
#
# print(f"x is {x}")