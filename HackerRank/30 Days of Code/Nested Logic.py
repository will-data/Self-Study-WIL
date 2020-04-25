from datetime import date

def fine(actualDate, expectedDate):
    if actualDate <= expectedDate:
        return 0
    else:
        if actualDate.month == expectedDate.month:
            return 15*(actualDate-expectedDate).days
# There is no function .months like days in datetime module, so be careful to not use it. You should get each dates' month first, and subtract it.
## DO NOT assume that there is always similar methods in module, it can make runtime error, as I did.
        elif actualDate.year == expectedDate.year:
            return 500*(actualDate.month-expectedDate.month)
        else:
            return 10000

actual = list(map(int, input().split()))
expected = list(map(int, input().split()))
actualDate = date(actual[2],actual[1],actual[0])
expectedDate = date(expected[2], expected[1], expected[0])
print(fine(actualDate, expectedDate))