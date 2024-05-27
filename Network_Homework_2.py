def binary_to_decimal(binary):
    decimal= 0
    for digit in binary:
        decimal=decimal* 2 + int(digit)
    return decimal
binary_number=input("Enter a binary number: ")
#Check if the input is a valid binary number:
if all(char=='0' or char=='1' for char in  binary_number):
    decimal_equivalent=binary_to_decimal(binary_number)
    print("The decimal equivalent of", binary_number, "is",decimal_equivalent)
else:
    print("invalid input, please enter a binary number: ")