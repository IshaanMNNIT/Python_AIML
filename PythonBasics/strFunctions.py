name = input("Enter the name ")
#Removes White spaces from the str
name = name.strip()
#Capitalize the first letter or alphabet of the str
name = name.capitalize()
print("Hello , ", name)
#Capitalize all the words in str
name = name.title()
print("Hello , ", name)

#All together
# name = name.strip().title()
# Or name = input("Enter the name ").strip().title()


name = "Ishaan Singh"
f_name,S_name = name.split(" ")
print(f_name,end=" ")
print(S_name)
