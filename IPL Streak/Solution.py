def solution(n,s):

    p=[]
    c=1
    for i in range(n-1):
        if s[i]==s[i+1] :
            c+=1
        else :
            p.append(c)
            c=1
    p.append(c)

    ans=0
    ind=0
    if s[0]=='1':
        ind=1

    while ind<len(p):
        c=p[ind]
        if ind-1>=0 :
            c+=p[ind-1]
        if ind+1<len(p) :
            c+=p[ind+1]

        ans=max(ans, c)
        ind+=2

    return ans

t=int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = solution(n,s)

    print(ans)
