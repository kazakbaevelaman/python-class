years=int(input("Provide num of years: "))

unit=int(input("""Pick your choice: 
    1 - days 
    2 - weeks   
    3 - hours 
    """))

if unit == 1:
    print(f"{years*365} days")
elif unit == 2:
    print(f"{years*52} weeks")
elif unit == 3:
    print(f"{years*365*24} hours")
else:
    print("Please pick correct num")

    

