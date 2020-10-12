# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
input = ["H","a","n","n","a","h"]
length = len(input) 
last_element_index = length - 1 
for i in range(length // 2):
    temp = input[i]
    input[i] = input[last_element_index - i] 
    input[last_element_index - i] = temp  
print(input)    