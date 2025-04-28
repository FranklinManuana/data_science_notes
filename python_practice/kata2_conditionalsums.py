def conditionalSum(values, condition):
    n = 0
    if len(values) > 0 and condition == "even":
        for i in values:
            if i%2 == 0:
                n += i
        return n
    if len(values) > 0 and condition == "odd":
        for i in values:
            if i%2 != 0:
                n +=i
        return n
    else:
        return n
   


print(conditionalSum([1, 2, 3, 4, 5], "even"))
print(conditionalSum([1, 2, 3, 4, 5], "odd"))
print(conditionalSum([13, 88, 12, 44, 99], "even"))
print(conditionalSum([], "odd"))