def fib(n):
    a = 0
    b = 1
    c = 0
    for i in range(0, n):
        c = a
        a += b
        b = c
    return a

def isEl(n):
    if(n >= 13 and n <= 18):
        return "You are eligible for Google Code-in"
    else:
        return "You are not eligible for Google Code-in"

def suffix(n):
    if(n == 1):
        return "st"
    elif(n == 2):
        return "nd"
    elif(n == 3):
        return "rd"
    else:
        return "th"

print ("Please enter your age: ")
age = int(input());
print ("Your age is", age)
print (isEl(age))
print ("The", str(age) + suffix(age) + " fibonacci number is", fib(age))
