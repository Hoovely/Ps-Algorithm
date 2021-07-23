// 백준_11054_가장 긴 바이토닉 부분 수열_DP_골드 3

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
			if(nums[i]>nums[j])
			{
				dp[i] = max(dp[i], dp[j] + 1);	
			}
		}
	}
	
	for(int i=1;i<n;i++)
	{
		for(int j=0;j<i;j++)
		{
			if(nums[i]<nums[j])
			{
				dp[i] = max(dp[i], dp[j] + 1);	
			}
		}
	}

	cout << *max_element(dp, dp+n);		
		
} 

//nums  1 5 2 1 4 3 4 5 2 1
//up    1 2 2 1 3 3 4 5 2 1
//down  1 1 2 3 2 3 2 1 4 5
//dp    1 2 3 4 3 4 4 5 6 7


