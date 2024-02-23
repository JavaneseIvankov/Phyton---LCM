def lcm(num1, num2):
    i = 1
    j = 1
    mylist = [num1, num2]
    mylist.sort()
    while mylist[0]*i != mylist[1]*j: #di sini index 0 sudah pasti angka yg paling kecil
        if mylist[0]*i > mylist[1]*j:
            j += 1
        elif mylist[0]*i < mylist[1]*j:
            i += 1
    return i*mylist[0]
