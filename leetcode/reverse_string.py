# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
input = ["H","a","n","n","a","h"]
length = len(input) 
last_element_index = length - 1 
for i in range(length // 2):
    temp = input[i]
    input[i] = input[last_element_index - i] 
    input[last_element_index - i] = temp  
print(input) 


# swift code solution 
class Solution {
    func reverseString(_ s: inout [Character]) {
        let length = s.count
        var lastElementIndex = length - 1 
        let halfOfTheArray: Int = length / 2
        for index in 0 ..< halfOfTheArray {
            var temp = s[index] 
            s[index] = s[lastElementIndex - index] 
            s[lastElementIndex - index] = temp
        
    }
        
         
    }
}