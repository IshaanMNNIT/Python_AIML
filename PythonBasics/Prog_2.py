s = "My userID is john17 and my 4 digit pin is 1234 which is secret."
t = ""
for i in range(len(s)):
    if s[i].isalpha():
        t += s[i]
    elif not s[i].isdigit():
        t += s[i]
    elif s[i].isdigit():
        # Check if digit is part of a word by examining neighboring characters
        if i>0 and t[i-1].isdigit():
            t += s[i]
        elif (i > 0 and s[i - 1].isalpha()) or (i < len(s) - 1 and s[i + 1].isalpha()):
            t += s[i]  # Keep digits within words unchanged
        else:
            t += 'x'  # Replace standalone numbers with 'x'
print(t)