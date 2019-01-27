def is_armstrong(number):
    numberstr = str(number)
    sum = 0

    for i in range(len(numberstr)):
        sum += int(numberstr[i])**len(numberstr)

    if sum == number:
        return True
    else:
        return False
