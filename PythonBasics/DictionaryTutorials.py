students = {"Hermione" : "Gryffindor",
            "Harry"    : "Gryffindor",
            "Ron"      : "Gryffindor",
            "Draco"    : "Slytherin"}
# print(students)
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

for student in students: #By default, student refer to key values of the dictionary students
    print(student, students[student], sep=" from ")

