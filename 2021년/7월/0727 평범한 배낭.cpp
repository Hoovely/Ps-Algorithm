#include <iostream>
#include <algorithm>
using namespace std;

int n, k, lst[2][101], dp[101][100001];

int main()
{
	cin >> n >> k;
	for(int i=1;i<n+1;i++)
	{
		cin >> lst[0][i] >> lst[1][i];
	}
	
	for(int i=1;i<n+1;i++)
	{
		for(int j=1;j<k+1;j++)
		{
			if(lst[0][i] > j) dp[i][j] = dp[i-1][j];
			else dp[i][j] = max(lst[1][i] + dp[i-1][j - lst[0][i]], dp[i-1][j]);
		}
	}
	
	cout << dp[n][k];
}

//6  4 3 5  무게 
//13 8 6 12 가치 
