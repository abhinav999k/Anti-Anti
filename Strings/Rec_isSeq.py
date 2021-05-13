Si=[1,2,4,5]
def isSeq(S,i,j):
    if(i==j):
        return True
    else:
        return ((isSeq(S,i+1,j) and S[i]==(S[i+1]-1)))

print(isSeq(Si,0,3))       