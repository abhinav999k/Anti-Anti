my_list=[10,5,3,6,5,89]
leng = len(my_list)-1
def maxi(L,i):
    if(i==0):
        return L[i]
    else:
        return max(L[i],maxi(L,i-1))

print(maxi(my_list,leng))