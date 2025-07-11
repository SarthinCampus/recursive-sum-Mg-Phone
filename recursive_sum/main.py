def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

user_input = input("Enter a positive number: ")

# Check if input is all digits (only positive integers)
if user_input.isdigit():
    num = int(user_input)
    print("Sum of digits:", sum_of_digits(num))
else:
    print("Error")
