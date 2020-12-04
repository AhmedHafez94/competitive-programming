s = "A man, a plan, a canal: Panama" 
s = list(s) 
s1 = [] 
for char in s:
    if ord(char)>= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122:
        s1.append(char.lower()) 

# s2 = list(reversed(s1)) 
s2 = s1 
s2.reverse()
print(s1 == s2) 