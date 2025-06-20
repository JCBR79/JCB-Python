try:
    number= int(input("Please enter an marks: "))
    if number > 75: print(f"grade is A.")
    elif number >=65: print(f"grade is B.")
    elif number >=55: print (f"grade is C.")
    else: print (f"grade is F.")
except  ValueError: print("Invalid Entry")