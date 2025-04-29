def sumLargestNumbers(n):
    n1 = max(n)
    n.remove(n1)
    n2 = max(n)
    return n1 + n2
print(sumLargestNumbers([10,4,34,6,92,2]))
