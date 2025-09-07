# Shira Choen 212079875
# Shira Erel 213173636

def digit_sum(n):
    digits = n.lstrip('-')

    if not digits.isdigit():
        return "invalid input"

    return sum(map(int, digits))

print("enter number:")
user_input = input().strip()
print(digit_sum(user_input))
