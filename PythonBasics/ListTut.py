def main():
    l = get_list(int(input("Enter the size of the list : ")))
    print_list(l)
    print("Length of the list : ", len(l))
def get_list(n):
    l=[]
    for i in range(n):
        l.append(input("Enter the value to be stored in the list : "))
    return l
def print_list(l):
    print("List : ",end=" ")
    for i in l :
        print(i+" ",end= " ")
main()

