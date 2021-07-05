// 백준_10971_외판원 순회 2_백트래킹_실버 2

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int min_num = 10000001;
int visited[10];
int urban[10][10];

void dfs(int start,int end,int sum,int cnt)
{
	if (cnt == n && start == end)
	{
		if (min_num > sum) min_num = sum;
		return;
	}
	
	for(int i = 0;i < n;i++)
	{
		if (urban[end][i] == 0 || visited[end] == 1) continue;
		
		if (urban[end][i] > 0 && visited[end] == 0)
		{
			sum += urban[end][i];
			visited[end] = 1;
			
			if (min_num > sum) dfs(start, i, sum, cnt+1);
			
			visited[end] = 0;
			sum -= urban[end][i];
		}
	}
}


int main()
{
	cin >> n;
	for(int i = 0; i<n ; i++)
	{
		for(int j = 0; j < n ; j++) cin >> urban[i][j];
	}
	
	for(int i = 0;i<n;i++) dfs(i,i,0,0);
	
	cout << min_num;
}
