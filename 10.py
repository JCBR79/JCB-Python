number = 0 
for number in range (0, 5):
    number = number + 1 
    
    student= int(input(f"Please enter marks for {number} : "))
    if student> 75: 
        print(f"grade of {number} is A.")
    elif student >=65: 
            print(f"grade of {number} is B.")
    elif student >=55: print (f"grade of {number} is C.")

    else: print (f"grade of {number} is F.")