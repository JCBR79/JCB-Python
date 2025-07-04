try:
    numerator_input=input("please enter the numerator:")
    numerator = float(numerator_input) #use floatto allow for decimal

    denominator_input=input("please enter the denominator:")
    denominator = float(denominator_input) # use floast to allow for decomals

    result=numerator/denominator

    print(f"You entered:Numerator={numerator}, Denomenator={denominator}")
    print(f"The result of the division is: {result}")

except ValueError:
    print("Invalid input. Please enter valid number for both numerator and denomenator")
except ZeroDivisionError:
    print("Can not devide by zero")
except Exception as e:
    #catch any other unexpected errors
    print(f"An unexpected error occuered: {e}") 