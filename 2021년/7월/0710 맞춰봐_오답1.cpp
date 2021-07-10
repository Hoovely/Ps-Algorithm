// ¹éÁØ_ 1248_¸ÂÃçºÁ_¹éÆ®·¡Å·_°ñµå 3
// ¿À´ä 1 

#include <iostream>
using namespace std;

int n, nums[10][10], result[10];
char lst[10][10];

bool check(int index)
{
	int sum = 0;
	for(int i=index;i>=0;i--)
	{
		sum += result[i];
		if(nums[i][index] == 0 and sum != 0) return false;
		if(nums[i][index] == 1 and sum <= 0) return false;
		if(nums[i][index] == -1 and sum >= 0) return false;
	}
	
	return true;
}

void solve(int index)
{
	if(n == index)
	{
		for(int i=0;i<n;i++) cout << result[i] << ' ';
		exit(0);	
	}
	
	if(nums[index][index] == 0)
	{
		result[index] = 0;
		solve(index+1);
		return;
	}
	
	for(int i=1;i<11;i++)
	{
		result[index] = i*nums[index][index];
		if (check(index) == true)
		{
			solve(index+1);
		}
	}
		
	
}

int main()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		for(int j=i;j<n;j++) 
		{
			cin >> lst[i][j];
			if(lst[i][j] == '+') nums[i][j] = 1;
			else if(lst[i][j] == '-') nums[i][j] = -1;
			else if(lst[i][j] == '0') nums[i][j] = 0;
		}
	}
	
	
	solve(0);
}
