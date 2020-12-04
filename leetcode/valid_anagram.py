s = "car"
t = "rat" 
length_s = len(s) 

d_s = {} 
d_t = {} 

for i in range(length_s):
    if s[i] in d_s :
        d_s[s[i]] = d_s[s[i]] + 1 
    else:
        d_s[s[i]] = 1 

    if t[i] in d_t :
        d_t[t[i]] = d_t[t[i]] + 1 
    else:
        d_t[t[i]] = 1        

print(d_s == d_t)