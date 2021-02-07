# urlify replace all spaces in string with '20%' 
ip = "mr john smith" 
def urlify(sentence):
    op = ""
    length = len(sentence) 
    sentence_array = list(range(length)) 
    for i in range(length):
        if sentence[i] == " ":
            sentence_array[i] = "%20" 
        else:
            sentence_array[i] = sentence[i] 
    return op.join(sentence_array) 


print(urlify(ip))                

