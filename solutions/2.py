for i in range(0,51):
    if sum(int(j) for j in list("{0:b}".format(i)))%2==1:
        print(i)
