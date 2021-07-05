// 백준_10819_차이를 최대로_백트래킹_실버 2

#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int n;
int max_num = 0;

int num[8];
vector<int> result;
bool visited[8];

void solve()
{
	if (result.size() == n)
	{
		int sum = 0;
		for (int i = 1; i < n; i++)
		{
			sum += abs(result[i-1] - result[i]);
		}
		
		max_num = max(max_num, sum);
	}
	for (int i = 0;i < n;i++)
	{
		if (visited[i]) continue;
		
		result.push_back(num[i]);
		visited[i] = true;
		solve();
		visited[i] = false;
		result.pop_back();
		
	}
}

int main()
{
	cin >> n;
	for (int i=0;i<n ;i++) cin >> num[i];
	
	solve();
	
	cout << max_num;
	
}
