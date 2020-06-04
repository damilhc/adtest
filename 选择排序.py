a=[33,12,233,12,3,11,23,4,1,441,2,4112,2231,3411,2,42112,23321]


for i in range(len(a)-1):
    min_index=i
    for j in range(i+1,len(a)):
        if a[min_index]>a[j]:
            a[min_index],a[j]=a[j],a[min_index]

print(a)





