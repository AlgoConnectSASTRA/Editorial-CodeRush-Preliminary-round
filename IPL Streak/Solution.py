def solution(n,s):
    streaks=[]
    startswith=True if s[0]=="1" else False
    count,prev=0,s[0]
    for i in s:
        if(i==prev):
            count+=1
        else:
            prev=i
            streaks.append(count)
            count=1
    streaks.append(count)
    if(len(streaks)==1):
        return streaks[0]
    if(len(streaks)<2):
        return streaks[0]+streaks[1]
    maxx=max(streaks[0]+streaks[1], streaks[-1]+streaks[-2])
    n=len(streaks)
    if(startswith):
        for i in range(0,n-2,2):
            maxx=max(streaks[i]+streaks[i+1]+streaks[i+2],maxx)
    else:
        for i in range(1,n-2,2):
            maxx=max(streaks[i]+streaks[i+1]+streaks[i+2],maxx)
    return maxx
