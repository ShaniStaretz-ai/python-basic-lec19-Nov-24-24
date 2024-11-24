def tuple_indexes_of_value(t1: tuple[int, ...], value: int, retrun=None) -> list[int]:
    # return [i for i in range(len(t1)) if t1[i] == value]
    result=[]
    for item in enumerate(t1):
        print(type (item))
        if item[1]==value:
            result.append(item[0])
    return result

print(
    f"the indexes of the value {5} in tuple {(40, 30, 10, 5, 2, 3, 5, 5, 8, 10)} are:{tuple_indexes_of_value((40, 30, 10, 5, 2, 3, 5, 5, 8, 10), 5)}")