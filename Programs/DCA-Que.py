class Solution:
    def __init__(self,s1,s2,n,res):
        self.s1 = s1
        self.s2 = s2
        self.n = n 
        self.res = res
    
    def prt(self):
        print(self.s1)
        print(self.s2)
        print(self.n)
        print(self.res)

    def solve(self):
        q1 = []
        q2 = []
        for i in self.s1:
            q1.append(i)
        #print(q1)
        for i in self.s2:
            q2.append(i)
        #print(q2)
        
        while(len(q1)!=0 and len(q2)!=0):
            if(len(q1)<=int(self.n)):
                for i in q1:
                    self.res += q1.pop(0)
            if(len(q2)<=int(self.n)):
                for i in q2:
                    self.res += q2.pop(0)
            if(len(q1)>int(self.n) and len(q2)>int(self.n)):    
                for i in range(int(self.n)):
                    self.res += q1.pop(0)
                for i in range(int(self.n)):
                    self.res += q2.pop(0)
                
        
        if(len(q1)==0 and len(q2)!=0):
            for i in q2:
                self.res += i
        elif(len(q2)==0 and len(q1)!=0):
            for i in q1:
                self.res += i

        return self.res
            

S1 = input()
S2 = input()
N = input()

s = Solution(S1,S2,N,"")
s.prt()
print(s.solve())
