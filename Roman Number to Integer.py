from collections import defaultdict
def_dict = defaultdict(list)
def_dict['I'] = [1, 0]
# def_dict['IV'] = 4
def_dict['V'] = [5, 1]
def_dict['X'] = [10, 2]
def_dict['L'] = [50, 3]
def_dict['C'] = [100, 4]
def_dict['D'] = [500, 5]
def_dict['M'] = [1000, 6]
L_1 = ['I', 'X', 'C', 'M']
L_2 = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
for _ in range(int(input())):
    n = input()
    flag = 0
    ans = 0
    for i in range(len(n)):
        try:
            k = n[i]
            num, index = def_dict[k]
            m = L_2[index+1:]
            if n[i+1] in m:
                flag = (-1)*num
            else:
                an = num + flag
                ans += an
                flag = 0
        except:
            k = n[i]
            num, index = def_dict[k]
            an = num + flag
            ans += an
    print(ans)