def feb():
    n1 = 0
    n2 = 1
    count = 10
    for i in range(2, count):
        i = n1 + n2
        n1 = n2
        n2 = i
        print("The feb series is :",i)
feb()


    



