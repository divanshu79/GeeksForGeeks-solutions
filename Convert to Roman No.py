from collections import defaultdict
def_dict = defaultdict(str)
def_dict[1] = 'I'
def_dict[2] = 'II'
def_dict[3] = 'III'
def_dict[4] = 'IV'
def_dict[5] = 'V'
def_dict[10] = 'X'
def_dict[50] = 'L'
def_dict[100] = 'C'
def_dict[500] = 'D'
def_dict[1000] = 'M'

def convert(n):
    if n <= 5:
        return def_dict[n]
    elif n < 10 and n > 5:
        k = ''
        p = n
        while p != 0:
            if p < 5:
                k += def_dict[p]
            elif p > 5 and p != 9:
                k += def_dict[5]
            else:
                pass



for _ in range(int(input())):
    n = int(input())
    print(convert(n))
