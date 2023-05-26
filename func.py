# function that keeps track of the sum of all the numbers that have been passed to it, and returns sum after exceding passed value
# and the difference of the sum and the passed value, and boolkean value if the sum is greater than the passed value

def sum(price):
    sum = 0
    while True:
        num = int(input("Enter a number: "))
        sum += num
        if sum > price:
            return sum, sum - price, True
            break

