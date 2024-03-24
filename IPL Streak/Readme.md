We know that we can make any contiguous number of 0s into 1s.  let's call this converting losing streak to a winning streak.

After a winning streak, comes a losing streak ( maybe even 1 loss) and after a losing streak, there should be a winning streak. So the patterns can be of types

W1 L1 W2 L2 W3...

1 0 1111 00 111...

or 

L1 W1 L2 W2 L3....

000 111 0 1 0...

We can observe that by converting a i-th losing streak to a winning streak, we are making W(i) + L(i) + W(i+1) as the new winstreak

eg. 111 00 1111 -> 111 11 1111

So, when we are at ith Winning streak, we convert the very next Losing streak and bridge ith and i+1th winning streak to form a new winning streak.

We try this for every ith winning streak and find the maximum of all these, to find our answer. 

Edge cases:
1. All are 0 / 1, we just convert all to winning streak
2. When L,W,L,.. case , before we compare winning streaks by bridging, we store L1+W1 value as initial max.
3. When .....,W,L case, before we compare winning streaks by bridging, we store W+L as initial max.
