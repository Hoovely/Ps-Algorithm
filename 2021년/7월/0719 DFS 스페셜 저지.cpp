// ¹éÁØ_16964_DFS ½ºÆä¼È ÀúÁö_DFS_°ñµå 5 

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, cnt = 0, visited[100001], result[100001], order[100001];
vector<int> graph[100001];

bool compare(int a, int b)
{
	return order[a] < order[b];
}

void dfs(int now)
{
	if(now != result[cnt])
	{
		cout << 0;
		exit(0);
	}
	
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		if(visited[next] == 0)
		{
			visited[next] = 1;
			cnt++;
			dfs(next);
		}
	}
}

int main()
{
	cin >> n;
	for(int i=0;i<n-1;i++)
	{
		int x,y;
		cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	for(int i=0;i<n;i++)
	{
		cin >> result[i];
		order[result[i]] = i + 1;
	}
	
	for(int i=1;i<n+1;i++)
	{
		sort(graph[i].begin(), graph[i].end(), compare);
	}
	
	visited[1] = 1;
	dfs(1);
	
	cout << 1;
}
