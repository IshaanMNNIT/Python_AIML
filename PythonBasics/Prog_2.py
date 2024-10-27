s = "My userID is john17 and my 4 digit pin is 1234 which is secret."
t = ""

for i in range(len(s)):
    if s[i].isalpha():  # If character is a letter, add it to t
        t += s[i]
    elif not s[i].isdigit():  # If it's not a letter or digit (e.g., space, punctuation), add it
        t += s[i]
    elif s[i].isdigit():  # If character is a digit
        # Check if it's part of a word or a standalone number
        if (i > 0 and s[i - 1].isalpha()) or (i < len(s) - 1 and s[i + 1].isalpha()):
            t += s[i]  # Keep it if it's part of a word
        else:
            t += 'x'  # Replace with 'x' if it's part of a standalone number

print(t)




