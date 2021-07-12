// 백준_13023_ABCDE_DFS_골드 5 
// 오답 1 

#include <iostream>
#include <vector>

using namespace std;

int n,m,visited[2000], flag = 0;
vector<int>graph[2000];

void dfs(int idx, int cnt)
{
	if (cnt == 4) 
	{
		flag = 1;
		return ;
	}
	
	for(int i=0;i<graph[idx].size();i++)
	{
		if(visited[graph[idx][i]] == 0)
		{
			visited[graph[idx][i]] = 1;
			dfs(graph[idx][i], cnt+1);
			visited[graph[idx][i]] = 0;
			
			if(flag) return;
		}
	}
}

int main()
{
	cin >> n >> m;
	for(int i=0;i<m;i++)
	{
		int x,y;
		
		cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	
	for(int i=0;i<n;i++)
	{
		visited[i] = 1;
		dfs(i,0);
		visited[i] = 0;
		
		if (flag) break;
	}
	
	cout << flag;
}
