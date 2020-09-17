# problem URL
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
digits = [1,2,3]
word = "" 
for element in digits:
    word = word + str(element) 
number = int(word) + 1 
number = str(number) 
print(list(number)) 
