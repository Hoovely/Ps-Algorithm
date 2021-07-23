// 백준_11722_가장 긴 감소하는 부분 수열_DP_실버 2 

#include <iostream>
#include <algorithm>
using namespace std;

int n, nums[1000], dp[1000];

int main()
{
	cin >> n;
	for (int i=0;i<n;i++) cin >> nums[i];
	fill(dp, dp+n, 1);
	
	for(int i=1;i<n;i++)
	{
		for(int j=0;j<i;j++)
		{
			if(nums[i] < nums[j])
			{
				dp[i] = max(dp[i], dp[j] + 1);
			}
		}
	}
	
	cout << *max_element(dp, dp+n);
} 

//10 30 10 20 20 10
//1  1  1  2  2  3


