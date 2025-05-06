#Task3:functions
def greet(name):
    print("Hello,",name)

greet("Paras")
greet("Nayan")

def add(a,b):
    result=a+b
    return result

sum1=add(5,7)
print("Sum = ",sum1)

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print("Is 4 even?",is_even(4))
print("Is 7 even?",is_even(7))