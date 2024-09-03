def solution_station_1(num):
    # calculate fibonacci sequence
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a
