import time


def decimaltobinary(decimal):
    binary_list = []
    while decimal is not 0:
        binary_list.append(decimal % 2)
        decimal = decimal // 2
    binary_list.reverse()
    return binary_list



print(decimaltobinary(1))
print(decimaltobinary(11))
print(decimaltobinary(59))
print(decimaltobinary(46))


# for i in range(50000):
#     current_time = time.localtime()
#     print(decimaltobinary(current_time.tm_hour),decimaltobinary(current_time.tm_min),decimaltobinary(current_time.tm_sec))
#     time.sleep(1)


    
