# try: statements in try block
# except: executed when error in try block

# example1. try...except blocks

try:
    a = 5
    b = 0
    print(a/b)
except TypeError: # specify type of exception
    print('TypeError Occurred')
except ZeroDivisionError:
    print('Division by zero not allowed')
except: # default except block needs to come after specific types
    print('Some error occured.')
print("OUt of try except blocks.")
#----------------------------------------------

# Example: try,except, else, finally blocks

try:
    x,y = 10, 2
    z = x/y
except ZeroDivisionError:
    print("except ZerioDivisionError block")
    print("Division by 0 not accepted")
except:
    print('Some error occurred.')
else:
    print("Division = ", z)
finally:
    print("Excecuting finally block")
    x = 0
    y = 0
print("Out of try, except, else and finally blocks")

#----------------------------------------------

# Excample 3 : Raise an Exception

try:
    x,y = 100 ,2
    z = x /2 
    if x > 10:
        raise ValueError(z)
except ValueError:
    print(z, "is out of allowed range")
else:
    print(z, "is within the allowed range")