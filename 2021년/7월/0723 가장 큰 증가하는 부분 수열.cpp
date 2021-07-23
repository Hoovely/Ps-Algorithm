// 백준_11055_가장 큰 증가하는 부분 수열_DP_실버 2 

#include <iostream>
#include <algorithm>
using namespace std;

int n, nums[1000], dp[1000];

int main()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		cin >> nums[i];
		dp[i] = nums[i];	
	}
	
	for(int i=1;i<n;i++)
	{
		for(int j=0;j<i;j++)
		{
			if(nums[i] > nums[j])
			{
				dp[i] = max(dp[i], dp[j] + nums[i]);
			}
		}
	}
	
	cout << *max_element(dp, dp+n);
}

//1 100 2 50 60 3 5 6 7 8
//1 101 3 53 113
//
//50 40 30 20 10
//50 40 30 20 10
//
//10 90  20 80  100
//10 100 30 110 210

 
