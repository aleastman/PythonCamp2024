
##exercise 1 Write a for loop, while loop, or a function (or all three!) to create a list of the first 10 numbers of the Fibonacci sequence.
def fibonacci(n): 
    fibonacci_series = [0,1]
    for i in range(0,n):
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series
n = 10
result = fibonacci(n)
print(result)

##2 an you now do it for the first 30 numbers?
n = 30
result = fibonacci(n)
print(result)

##3 return true if there is no e in 'word', else false
def has_no_e(word):
    if "e" in word: return False 
    else: return True

has_no_e("ope")
##4  return true if there is e in 'word', else false
def has_e(word):
    if "e" in word: return True
    else: return False 
has_e("ope")

##5 return true if word1 contains all letters from word2, else false
def uses_all(word1, word2):
    for char in word1:
    if char in word2: return True
    else: return False


##6 return true if word1 uses only the letters in word2, else false
def uses_only(word1, word2):
    if len(word1) == len(word2): return True
    else: return False 

uses_only("quack", "quack")


#7 return true or false 
# Is the word in alphabetical order? return True if yes, False if not. 
# Hint: check the methods for lists
def is_abecedarian(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True