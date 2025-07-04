class NegativeNumberError(ValueError):
    """Custom exception raised when a negative number is entered"""
    pass

def get_positive_number():
    """Asks the user for a number and raises a NegativeNumberError if positive number is raised"""
    while True:
        try:
            num_str = input("Please enter a positive number: ")
            number = float(num_str) #use float to allow decimal numbers

            if number < 0:
                raise NegativeNumberError("Number must be positive")
            return number
        
        except NegativeNumberError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid Input. Please enter a valid number")
        
if  __name__ == "__main__":
    try:
        positive_num = get_positive_number()
        print(f"You entered a posotive number:{positive_num}")
    except NegativeNumberError as e:
        print(f"Caught an error in the main scripts: {e}")
    except Exception as e:
        print(f"An unexpected error occured:{e}")

