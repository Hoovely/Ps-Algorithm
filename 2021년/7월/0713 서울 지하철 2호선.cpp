// 백준_16947_서울 지하철 2호선_DFS_골드 3

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, start, visited[3001], d[3001];
int flag = 0;
vector<int> graph[3001];

void dfs(int now, int cnt)
{
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		if(visited[next] == 0)
		{
			visited[next] = 1;
			dfs(next, cnt+1);
			if(flag == 1)
			{
				d[now] = 0;
				return;
			}
		}
		else
		{
			if(cnt >= 3 and start == next)
			{
				fill(d+1, d+n+1,1);
				flag = 1;
				d[now] = 0;				
				return ;
			}
		}
	}
}

void sum_distance(int now, int dis)
{
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		
		if(visited[next] != 0) continue;
		
		if(d[next] == 0)
		{
			d[now] = dis;
			cout << dis << ' ';
			return;
		}
		else
		{
			visited[next] = 1;
			sum_distance(next, dis+1);
		}
	}
}

int main()
{
	cin >> n;

	for(int i=0;i<n;i++)
	{
		int a,b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	
	for(int i=1;i<n+1;i++)
	{
		fill(visited+1, visited+n+1,0);
		
		start = i;
		
		visited[i] = 1;
		dfs(i,1);
		if (flag == 1) break;
	}
	
	for(int i=1;i<n+1;i++)
	{
		if (d[i] == 0) cout << 0 << ' ';
		else
		{
			fill(visited+1, visited+n+1,0);
			sum_distance(i, 1);
		}
	}
}
