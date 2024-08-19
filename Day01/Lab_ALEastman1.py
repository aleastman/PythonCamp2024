#Convert positive integer to base 2
def binarify(num): 
    if num <= 0: 
        return '0'
    digits = []
    # YOUR CODE HERE
    return ''.join(digits)

    
#Convert positive integer to a string in any base
def int_to_base(num, base):
    if num <= 0:  
        return '0' 
    digits = []
    # YOUR CODE HERE
    return ''.join(digits)
    
#Take a string-formatted number and its base and return the base-10 integer
def base_to_int(string, base):
    if string == "0" or base <= 0 : 
        return 0 
    result = 0 
    # YOUR CODE HERE
    return result
    
#Add two numbers of different bases and return the sum
def flexibase_add(str1, str2, base1, base2):
    # YOUR CODE HERE
    return result 

#Multiply two numbers of different bases and return the product
 def flexibase_multiply(str1, str2, base1, base2):
    # YOUR CODE HERE
    return result 
     
#Given an integer, return the Roman numeral version
def romanify(num):
    number = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
     
    while num:
        div = num // number[i]
        number %= num[i]
 
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
    return result