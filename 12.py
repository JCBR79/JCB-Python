number = 0 
for number in range(0, 5): 
    number=int(input(f"Please enter marks for {number} : "))
    while number<0 or number>100:
        print("invalid mark")
        number= int(input(f"Please enter marks for {number} : "))
    if number> 75:
            print(f"grade of {number} is A.")
    elif number >=65:
            print(f"grade of {number} is B.")
    elif number >=55: print (f"grade of {number} is C.")

    else: print (f"grade of {number} is F.")