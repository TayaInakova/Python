
def declension(num, end: list[str]):
    if num % 10 == 1 and num % 100 != 11:
        return end[0]
    elif (num % 10 == 2 or num % 10 == 3 or num % 10 == 4) and (num % 100 != 12 or num % 100 != 13 or num % 100 != 14):
        return end[1]
    else:
        return end[2]
