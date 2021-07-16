// 백준_1707_이분 그래프_DFS_골드 4
// 오답 1 

#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int v,e,flag,visited[20001], color[20001];
vector<int> graph[20001];

void dfs(int now)
{
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		if(color[next] == 0)
		{
			if(color[now] == 1) color[next] = 2;
			else color[next] = 1;
			dfs(next);
		}
	}
}

void solution(int now)
{
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		
		if(color[now] == color[next])
		{
			flag = 1;
			return;
		}
		
		if (visited[next] == 0)
		{
			visited[next] = 1;
			solution(next);
		}
		
		if (flag == 1) return;
	}
}

int main()
{
	int k,x,y;
	cin >> k;
	while(k--)
	{
		cin >> v >> e;
		
		for(int i=1;i<v+1;i++)
		{
			graph[i].resize(0);
			color[i] = 0;
			visited[i] = 0;
		}
		
		for(int i=0;i<e;i++)
		{
			cin >> x >> y;
			graph[x].push_back(y);
			graph[y].push_back(x);
		}
		
		for(int i=1;i<v+1;i++)
		{
			if(color[i] == 0)
			{
				color[i] = 1;
				dfs(i);
			}
		}
		
		flag = 0;
		for(int i=1;i<v+1;i++)
		{
			if(visited[i] == 0)
			{
				visited[i] = 1;
				solution(i);
			}
			if(flag == 1) break;
		}
		
		if (flag == 0) cout << "YES" << "\n";
		else cout << "NO" << "\n";
	}
}
