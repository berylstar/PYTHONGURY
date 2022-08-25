list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    idx = i -1

    if list[idx] == 4:
        print("this is 4")
        continue
    if list[idx] % 2 == 0:
        print(list[idx])
    else:
        print(f"not {list[idx]}")