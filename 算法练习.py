
a=[33,12,233,12,3,11,23,4,1,441,2,4112,2231,3411,2,42112,23321]

def maopao(alist):
    n=len(alist)
    for i in range(n-1):
        for j in range(n-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]

def select_sort(alist):
    n=len(alist)
    for i in range(n-1):
        for j in range(i+1,n):
            if alist[i]>alist[j]:
                alist[i],alist[j]=alist[j],alist[i]




maopao(a)
print(a)

select_sort(a)
print(a)