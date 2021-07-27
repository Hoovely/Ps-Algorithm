#include <iostream>
#include <algorithm>
using namespace std;

int n, dp[21][100], lst[2][21];

int main()
{
	cin >> n;
	for(int i=1;i<n+1;i++) cin >> lst[0][i]; 
	for(int i=1;i<n+1;i++) cin >> lst[1][i];
	
	for(int i=1;i<n+1;i++)
	{
		for(int j=0;j<100;j++)
		{
			if(lst[0][i] > j) dp[i][j] = dp[i-1][j];
			else dp[i][j] = max(lst[1][i] + dp[i-1][j-lst[0][i]], dp[i-1][j]);
		}
	}
	
	cout << dp[n][99];
} 
