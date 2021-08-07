##Return this number if it is a single digit
##The sum of the two digits
def sumOfDoubleEvenPlace(number):
    numberList = list(map(int, str(number)))
    evenList = list()
    for i in numberList[-2: :-2]:
        if i >= 5:
            digit = i * 2 % 10 + 1
        else:
            digit = i
        evenList.append(digit)
    return sum(evenList)


##Return sum of odd place digits in number
def sumOfOddPlace(number):
    numberList = list(map(int, str(number)))
    oddList = list()
    for i in numberList[-1: :-2]:
        oddList.append(i)
    return sum(oddList)


##Return True if the card number is valid
def isValid(number):
    if (sumOfDoubleEvenPlace(number)\
            + sumOfOddPlace(number)) % 10 == 0:
        return True
    else:
        return False

def main():
    while True:
        try:
            number = int(input("Please input a credit card number"))
            if number > 0:
                break
            else:
                print("Please input a positive number")
        except:
            print("Please input a valid number, try again")
    
    if isValid(number):
        print('this is a valid credit card number')
    else:
        print('This is not a valid credit card number')

main()12