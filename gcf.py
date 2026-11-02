def find_gcd(a, b):
    while b:
        a, b = b, a%b
    return a





number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))

gcf= find_gcd(number1,number2)
