#include <iostream>

using namespace std;

int n, s[10][10], nums[10];
char lst[10][10];

bool check(int index)
{
	int sum = 0;
	for(int i=index;i>-1;i--)
	{
		sum += nums[i];
		if (s[i][index] == 0 && sum != 0) return false;
		if (s[i][index] == 1 && sum <= 0) return false;
		if (s[i][index] == -1 && sum >= 0) return false;
	}
	return true;
}

void solve(int index)
{
	if (index == n)
	{
		for(int i=0;i<n;i++) cout << nums[i] << " ";
		exit(0);
	}
	
	if (s[index][index] == 0)
	{
		nums[index] = 0;
		solve(index+1);
		return;
	}
	
	for(int i=1;i<11;i++)
	{
		nums[index] = i*s[index][index];
		if (check(index) == true) solve(index+1);
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
			if(lst[i][j] == '+') s[i][j] = 1;
			else if(lst[i][j] == '-') s[i][j] = -1;
			else s[i][j] = 0;
		}
	}
	
	solve(0);
}

