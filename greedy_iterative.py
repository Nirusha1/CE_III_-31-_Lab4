def GreedyIterative(start_time, finish_time):
    #start_time=[1,3,0,5,3,5,6,8,8,2,12]
    #finish_time=[4,5,6,7,9,9,10,11,12,14,16]
    n=len(start_time)
    A=[0]
    k=0

    for i in range(0,n):
        if (start_time[i] >= finish_time[k]):
            A.append(i)
            k=i
    return A


#GreedyIterative()

    
