"""
Base convertor: recieves an integer as decimal value & base, then value is converted to corresponding base
function takes 2 args (value,base)
f(int,base): value->base representation
ex: f(10,2): 10 -> 1010 (binary)
"""

import sys
from stack import Stack

#function uses stack data structure to store integer sequences

def BaseConvertor(dec_value,base):

    values = "0123456789ABCDEF"
    s = Stack()
    result = ''


    while dec_value != 0:
        value = values[dec_value % base]
        s.add(value)
        dec_value = dec_value//base

    while s.isEmpty():
        get_last_item = s.remove()
        result +=get_last_item

    return result


if __name__ == "__main__":

    dec_value = sys.argv[-2] 
    base = sys.argv[-1]
    print(BaseConvertor(dec_value,base))



