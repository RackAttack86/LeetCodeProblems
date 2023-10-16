# Convert to strings
import math


def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

# Reverse int without converting to string
def rev(num: int):
    return int(num != 0) and ((num%10) * (10**int(math.log(num, 10))) + rev(num // 10))

# Check is palindrome without converting to string
def isPalindrome2(x: int) -> bool:
    return x == rev(x)

result = isPalindrome(121)
print(result)
assert(result == True)

result = isPalindrome2(121)
print(result)
assert(result == True)