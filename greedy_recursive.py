#start_time=[1,3,0,5,3,5,6,8,8,2,12]
#finish_time=[4,5,6,7,9,9,10,11,12,14,16]
#n=len(start_time)
#A=[]
#   k=-1

A=[]
def GreedyRecursive(start_time, finish_time, k, n):    
    m=k+1
    while (m<n and start_time[m]<finish_time[k]and k>=0):
        m=m+1
    if (m<n):
        A.append(m)
        
        GreedyRecursive(start_time, finish_time, m, n)
    else:
        return None
    return A

#GreedyRecursive(start_time, finish_time, k, n)
