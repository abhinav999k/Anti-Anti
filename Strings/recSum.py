Si = [1,2,3,4,5]
def sum(S,i,j):
    if(i==j):
        return S[i]
    else:
        return sum(S,i+1,j)+S[i]

print(sum(Si,0,len(Si)-1))