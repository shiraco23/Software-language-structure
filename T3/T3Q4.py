# Shira Choen 212079875
# Shira Erel 213173636

# Regular recursion
def is_palindrome_regular(num_str):
    if len(num_str) <= 1:
        return True
    if is_palindrome_regular(num_str[1:-1]) and num_str[0] == num_str[-1]:
        return True
    
    return False

def isPalindrome_regular(num):
    return is_palindrome_regular(str(num))


# Tail recursion
def is_palindrome_tail(num_str):
    if len(num_str) <= 1:
        return True
    if num_str[0] != num_str[-1]:
        return False
    
    return is_palindrome_tail(num_str[1:-1])

def isPalindrome_tail_recursive(num):
    return is_palindrome_tail(str(num))

# testing
print(f"123454321 רגילה: {isPalindrome_regular(123454321)}")
print(f"123454321 זנבית: {isPalindrome_tail_recursive(123454321)}")