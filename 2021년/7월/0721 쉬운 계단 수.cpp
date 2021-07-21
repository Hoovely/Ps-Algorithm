// 백준_10844_쉬운 계단 수_DP_실버 1 

#include <iostream>
using namespace std;

int n;
long long dp[101][10];
long long mod = 1000000000;

int main()
{
	cin >> n;
	for(int i=1;i<10;i++) dp[1][i] = 1;
	for(int i=2;i<n+1;i++)
	{
		for(int j=0;j<10;j++)
		{
			if(j==0) dp[i][j] = dp[i-1][j+1];
			else if(j==9) dp[i][j] = dp[i-1][j-1];
			else dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%mod;
		}
	}
	
	long long sum = 0;
	for(int i=0;i<10;i++)
	{
		sum += dp[n][i];
	}
	
	cout << sum%mod;

}
