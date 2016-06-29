
from pyvogue import Transaction


s = Transaction()


'''The first param is the transaction to be queried
    the second param is the result format
    the third param is the option to decode to python dictionary'''

#r = s.getall('xxxxxxxxxx','json')
r = s.getall('xxxxxxxx','json',True)
print(r)
