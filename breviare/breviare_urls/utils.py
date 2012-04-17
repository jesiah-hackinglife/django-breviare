BASE2 = "01"
BASE10 = "0123456789"
BASE16 = "0123456789ABCDEF"
BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"

def baseconvert(number,fromdigits,todigits):
    """ converts a "number" between two bases of arbitrary digits
    """

    if str(number)[0]=='-':
        number = str(number)[1:]
        neg=1
    else:
        neg=0

    # make an integer out of the number
    x=0
    for digit in str(number):
       x = x*len(fromdigits) + fromdigits.index(digit)
    
    # create the result in base 'len(todigits)'
    if x == 0:
        res = todigits[0]
    else:
        res=""
        while x>0:
            digit = x % len(todigits)
            res = todigits[digit] + res
            x = int(x / len(todigits))
        if neg:
            res = "-"+res

    return res