for _ in range(int(input())):
    n = input()
    ans = 0
    def_dict = {}
    def_list = []
    for i in n:
        try:
            if def_dict[i] > 0:
                j = 0
                while True:
                    if def_list[j] != i:
                        def_dict[def_list[j]] = 0
                        def_list.pop(0)
                    else:
                        def_list.pop(0)
                        def_list.append(i)
                        break
            else:
                def_dict[i] = 1
                def_list.append(i)
                if len(def_list) > ans:
                    ans = len(def_list)

        except:
            def_dict[i] = 1
            def_list.append(i)
            if len(def_list) > ans:
                ans = len(def_list)
    print(ans)