try:
    x = int(input("What's x ? "))

except ValueError:
    print("Entered value of x is not integer . ")
else:
    print(f"x is {x}")


#we could get NameError if we omit the use of
#else statement because if we get a ValueError exception
#there is nothing that is assigned to x and hence it is undefined
#this may lead to NameError Exception
