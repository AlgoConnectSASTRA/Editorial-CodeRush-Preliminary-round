def solution(m,S):
    maxc=c=0
    vowels="aeiou"
    for i in S:
        if(i in vowels):
            c+=1
        else:
            c=0
        maxc=max(c,maxc)

    if maxc>=m:
        return 'HAPPY'
    else
        return 'SAD'
