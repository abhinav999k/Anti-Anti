def RedOrGreen(self,N,S):
    count_f = 0
    count_s =0
    main=0
    for f in S:
        if(f == 'R'):
            count_f+=1
        else:
            count_s+=1
    
    if(count_f>= count_s):
        main = count_s
        return main
    else:
        main = count_f
        return main

print(check("RGGGGRRGRG"))