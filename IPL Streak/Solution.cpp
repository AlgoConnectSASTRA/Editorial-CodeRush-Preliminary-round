#include<bits/stdc++.h>
using namespace std;

long solution(long n, string s) {
    
    vector<long> p;
    
    long c=1;
    
    for( long i=0; i<n-1; i++)
    {
        if( s[i]==s[i+1] )
            c++;
        else
        {
            p.push_back(c);
            c=1;
        }
    }
    p.push_back(c);
    
    long ans=0, ind= s[0]=='0' ? 0:1, l=p.size();
    
    for( ; ind<l; ind+=2 )
    {
        c=p[ind];
        
        if( ind-1>0 )
            c+=p[ind-1];
        if( ind+1<l )
            c+=p[ind+1];
        
        ans=max( ans, c);
    }
    
    return ans;

}

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        long n;
        string s;

        cin >> n >> s;
        cout << solution( n, s) << endl;
    }

    return 0;
}