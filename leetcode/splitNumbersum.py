def splitNumbersum(ip):
    ip = str(ip)
    length = len(ip) 
    if length == 1:
        return ip
    sum = 0 
    index = length - 1 
    while index >= 0 :
        sum = sum + int(ip[index])
        index = index - 1
    
    print(sum)   
    return splitNumbersum(sum) 

print(splitNumbersum(59845))

