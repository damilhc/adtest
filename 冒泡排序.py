import time
star=time.time()
a=[33,12,233,12,3,11,23,4,1,441,2,4112,2231,3411,2,42112,23321]

# a=[1, 2, 2, 3, 4, 11, 12, 12, 23, 33, 233, 441, 2231, 3411, 4112, 23321, 42112]
for k in range(len(a)-1):
    count=0
    for i in range(len(a)-1-k):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            count+=1
    if count==0:
        break


print(a)
print(time.time()-star)