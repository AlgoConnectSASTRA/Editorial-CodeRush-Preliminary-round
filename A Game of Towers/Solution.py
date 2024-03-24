def ntowers(n,arr):
    towers=[]
    def f(x):
        l,r=0,len(towers)-1
        ans=len(towers)
        while(l<=r):
            mid=(l+r)//2
            if(towers[mid]>=x):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
    for i in arr:
        ind=f(i)
        if(ind==len(towers)):
            towers.append(i)
        else:
            towers[ind]=i
    return len(towers)    

def solution(n, books): 
    arr=books
    alice=[arr[i] for i in range(0,n,2)]
    bob=[arr[i] for i in range(1,n,2)]
    q1,q2=ntowers(n//2,alice),ntowers(n//2,bob)
    if(q1<q2):
        return "ALICE"
    elif(q1==q2):
        return "DRAW"
    else:
        return "BOB"
