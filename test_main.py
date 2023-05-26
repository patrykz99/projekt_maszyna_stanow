from func import sum    # import the function from func.py


if __name__ == "__main__":    # if the program is run directly
    price = int(input("Enter a price: "))
    sum, diff, state = sum(price)    # call the function and assign the returned values to variables, state is a boolean value  
    print("Sum:", sum, "Difference:", diff, "State:", state)    # print the values