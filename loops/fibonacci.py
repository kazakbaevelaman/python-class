limit = int(input("Enter the limit: "))

first = 0
second = 1

if first <= limit:
    print(first)

if second <= limit:
    print(second)

next = first + second 

while next <= limit:
    print(next)
    first = second 
    second = next
    next = first + second 



    