def find_odd(val):
    val = sorted(val, key=int)
    temp_val = val[0]
    counter = 0
    for i, number in enumerate(val):
        if not number in val:
            # number repeated odd times
            return temp_val
        else:
            if number == temp_val:
                counter = counter+1
            else:
                if counter % 2 != 0:
                    return temp_val
                counter = 1
                temp_val = number
    return temp_val

# def effective_way(val):
#     for i in val:
#         if val.count(i)%2!=0:
#             return i