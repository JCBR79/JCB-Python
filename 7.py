try:
    number = int(input("Please enter an integer:"))
    if number > 0: 
        print(f"The number {number} is positive.")
    elif number < 0: print(f"The number {number} is negative.")
    else: 
        print(f"The number {number} is zero.")
except ValueError: print("Invalid input. Please enter a valied whole number.")
