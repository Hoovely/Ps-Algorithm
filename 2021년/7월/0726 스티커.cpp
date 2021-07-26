// 백준_9465_스티커_DP_실버 2

#include <iostream>
#include <algorithm>
using namespace std;

int t, n, dp[2][100001];

int main()
{
	cin >> t;
	while(t--)
	{
		cin >> n;
		
		for(int i=0;i<2;i++)
		{
			for(int j=1;j<n+1;j++)
			{
				cin >> dp[i][j];
			}
		}
			
		for(int i=2;i<n+1;i++)
		{
			dp[0][i] += max(dp[1][i-1], dp[1][i-2]);
			dp[1][i] += max(dp[0][i-1], dp[0][i-2]);
		}
		
		cout << max(dp[0][n], dp[1][n]) << endl;
		
	}
} 
