
def solution_station_4(num):
    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2, (num//2)+1):
                if (num % i) == 0:
                    return False
        else:
            return True