// 백준_1912_연속합_DP_실버 2

#include <iostream>
#include <algorithm> 
using namespace std; 

int n, nums[100000];

int main()
{
	cin >> n;
	for(int i=0;i<n;i++) cin >> nums[i];
	
	for(int i=1;i<n;i++)
	{
		nums[i] = max(nums[i], nums[i-1] + nums[i]);
	}
	
	cout << *max_element(nums, nums+n);
}

