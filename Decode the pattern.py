from collections import defaultdict
def_dict = defaultdict(str)
for i in range(21):
    if i == 0:
        def_dict[i+1] = '1'
    else:
        char = ''
        count = 0
        ans = ''
        for j in range(len(def_dict[i])):
            k = def_dict[i]
            if char == '':
                char = k[j]
                count += 1
            elif char == k[j]:
                count += 1
            elif char != k[j]:
                ans += str(count) + char
                char = k[j]
                count = 1
        ans += str(count) + char
        def_dict[i+1] = ans

for _ in range(int(input())):
    n = int(input())
    print(def_dict[n])
