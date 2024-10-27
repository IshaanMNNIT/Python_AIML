# String Compression
s="aabcccccaaa"
print(s)
i=0
t=""
count = 0
while i<len(s):
    t=t+s[i]
    j=i
    while j<len(s)-1:
        if s[j]==s[j+1]:
            count+=1
            j+=1
        else:
            i=j+1
            break
    i=j+1
    t+=str(count+1)
    count=0
print(t)
