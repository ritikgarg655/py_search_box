#include<bits/stdc++.h>
using namespace std;

// template 
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<pii> vii;

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define rep(i,a,b) for(int i=a;i<b;i++)
#define repv(i,v) for(int i=0;i<v.size();i++)
#define reps(i,s) for(int i=0;i<s.length();i++)
#define allv(v) v.begin(),v.end()
#define alla(arr,sz) arr,arr+sz
#define rev(v) reverse(allv(v))
#define reva(a) reverse(alla(a))


void solve(){
	 int n;
        cin>>n;
       char c[n][n]={};
       rep(i,0,n)
       {
           fo(j,0,n)
           {
               cin>>c[i][j];
           }
       }
       int count=0;
       if(c[0][1]=='0'&&c[1][0]=='0')
       {
           if(c[n-1][n-2]=='0')
           count++;
           if(c[n-2][n-1]=='0')
           count++;
           cout<<count<<endl;
           if(c[n-1][n-2]=='0')
           cout<<n<<" "<<n-1<<endl;
           if(c[n-2][n-1]=='0')
           cout<<n-1<<" "<<n<<endl;
       
       return;
       
           
       }
        else if(c[0][1]=='1'&&c[1][0]=='1')
       {
           if(c[n-1][n-2]=='1')
           count++;
           if(c[n-2][n-1]=='1')
           count++;
           cout<<count<<endl;
           if(c[n-1][n-2]=='1')
           cout<<n<<" "<<n-1<<endl;
           if(c[n-2][n-1]=='1')
           cout<<n-1<<" "<<n<<endl;
       
       return;
       
           
       }
       else
       {
           int one=0;int zero=0;
           if(c[n-1][n-2]=='1')
           one++;else zero++;
              if(c[n-2][n-1]=='1')
           one++;else zero++;
           
           if(one==2)
           {
               cout<<1<<endl;
               if(c[0][1]=='1')
               cout<<"1 2"<<endl;
               else
               cout<<"2 1"<<endl;
               continue;
           }
           else if(zero==2)
           {
               cout<<1<<endl;
               if(c[0][1]=='0')
               cout<<"1 2"<<endl;
               else
               cout<<"2 1"<<endl;
               continue;
           }
           else
           {
               int a,b,cc,d;
               if(c[0][1]=='0')
               {
               a=1;b=2;
                   
               }
               else{
               a=2;b=1;}
               if(c[n-1][n-2]=='1'){
               cc=n;d=n-1;}
               else{
               cc=n-1;d=n;}
               cout<<2<<endl;
               cout<<a<<" "<<b<<endl;
               cout<<cc<<" "<<d<<endl;
               
           }
           
           
       }
}

int main(){
	ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	int t;
	// t = 1;
	cin>>t;
	while(t--){
		solve();
	}
}