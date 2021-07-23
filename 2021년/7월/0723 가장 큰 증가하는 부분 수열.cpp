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
		int point = 0;
		for(int j=0;j<i;j++)
		{
			if(nums[i] > nums[j] and nums[j] > point)
			{
				point = nums[j];
				dp[i] = max(dp[i], nums[i] + nums[j]);
			}
		}
	}
	
	cout << *max_element(dp, dp+n);
}


