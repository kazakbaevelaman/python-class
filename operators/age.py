age = int(input("Please enter your age: "))

if age < 0:
    print("Please enter a valid age!")
elif age <= 13:
    print("child")
elif age < 18:
    print("teenager")
elif age < 65:
    print("adult")
else:
    print("elder")



