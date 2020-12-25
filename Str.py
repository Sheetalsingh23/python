# Python implementation to check string 
# for specific characters 
  
# function to check string 
def check(s, arr): 
    result = [] 
    for i in arr: 
        
        # for every character in char array 
        # if it is present in string return true else false 
        if i in s: 
            result.append("True") 
        else: 
            result.append("False") 
    return result 
  
  
# Driver Code 
s = "@geeksforgeeks123"
arr = ['e', 'r', '1', '7'] 
print(check(s, arr)) 
