#Assuming I can not use the function range

def add(x,y):
    return x + y

def multiplication(x,y):
    const_x = x
    while y > 1:
        x = add(x, const_x)
        y -= 1

    return x

def power(x,y):
    result = x
    while y > 1:
        result = multiplication(result, x)
        y -= 1

    return result

#Testing
a = power(6, 9)
print(a)
