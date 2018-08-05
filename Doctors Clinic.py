for _ in range(int(input())):
    no_fo_cos, time_int = map(int, input().split())

    arrival_time = []
    exit_time = []
    waiting_time = []
    consume_time = 10
    if time_int < 10:
        for i in range(no_fo_cos):
            if i == 0:
                arrival_time.append(0)
                exit_time.append(10)
                waiting_time.append(0)
            else:
                arrival_time.append(i*time_int)
                x = exit_time[i-1]+10
                if arrival_time[i] > x:
                    exit_time.append(arrival_time[i]+10)
                else:
                    exit_time.append(x)
                waiting_time.append(exit_time[i-1]-arrival_time[i])
        print(waiting_time[no_fo_cos-1])
    else:
        print(0)