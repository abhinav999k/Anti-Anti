#User function Template for python3
class Solution:
    def revStr (ob, S):
        x = ""
        list1=[]
        list1[:] = S
        list1.reverse()
        for i in list1:
            x+=i
        return x
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.revStr(S))
# } Driver Code Ends

shortcut
S="hello"
S=S[::-1]
print(S)