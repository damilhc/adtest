# import time
# start=time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#
#         c=1000-a-b
#         if a**2+b**2==c**2:
#             print("a,b,c",a,b,c)
# print('time:',(time.time()-start))



#冒泡

def mappao(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    print(alist)

a=[33,12,233,12,3,11,23,4,1,441,2,4112,2231,3411,2,42112,23321]

mappao(a)


def select_sort(alist):
    n =len(alist)
    for i in range(n-1):
        for j in range(i+1,n):
            if alist[i]>alist[j]:
                alist[i],alist[j]=alist[j],alist[i]
    print(alist)

select_sort(a)


