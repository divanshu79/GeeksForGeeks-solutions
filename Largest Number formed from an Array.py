from collections import defaultdict
import pandas as pd
import numpy as np
for _ in range(int(input())):
    n = int(input())
    arr = list(map(str, input().split()))
    def_dict = defaultdict(list)

    for i in arr:
        def_dict[i[0]].append(i)

    for i in range(9, 0, -1):
        # k = np.array(def_dict[i])
        # df = pd.DataFrame(k)
        # print(df)
        pass

