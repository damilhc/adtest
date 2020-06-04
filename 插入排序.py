a=[33,12,233,12,3,11,23,4,1,441,2,4112,2231,3411,2,42112,23321]

def insert_sort(alist):
    n=len(alist)
    for i in range(1,n):
        while i >0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
            else:
                break
            i-=1

insert_sort(a)
print(a)