#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, dp[100];
vector<pair<int,int> >lst;

void input()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{	
		int x,y;
		cin >> x >> y;
		lst.push_back(make_pair(x,y));
	}
}

void solution()
{
	sort(lst.begin(),lst.end());
	for(int i=0;i<n;i++)
	{
		dp[i] = 1;
		for(int j=0;j<i;j++)
		{
			if(lst[i].second > lst[j].second)
			{
				dp[i] = max(dp[i], dp[j]+1);
			}
		}
	}
	
	cout << n-*max_element(dp, dp+100);
}

int main()
{
	input();
	solution();
}
