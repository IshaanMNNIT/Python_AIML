#Custom Sort Program
def custom_sort(l,rev):

    if not rev: # Default Case when reverse if false
        for i in range(len(l)):
            for j in range(0,len(l)-1):
                if l[j][1]>(l[j + 1])[1]:
                    l[j],l[j+1]=l[j+1],l[j]

    else :
        for i in range(len(l)):
            for j in range(0,len(l)-1):
                if l[j][1]<(l[j + 1])[1]:
                    l[j],l[j+1]=l[j+1],l[j]

    return l




l = [(1,2),(3,1),(5,4)]
print(l)
print(custom_sort(l,False))
print(custom_sort(l,True))
