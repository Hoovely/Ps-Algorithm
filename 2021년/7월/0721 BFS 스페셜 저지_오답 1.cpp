// 백준_ 16940_BFS 스페셜 저지_BFS_골드 4
// 오답 1 

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm> 
using namespace std; 

int n, visited[100001], lst[100001], order[100001];
vector<int> graph[100001];
queue<int> que;

bool compare(int a, int b)
{
	return order[a] < order[b];
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
		cin >> lst[i];
		order[lst[i]] = i+1;
	}
	
	for(int i=1;i<n+1;i++)
	{
		sort(graph[i].begin(), graph[i].end(),compare);
	}
	
	que.push(1);
	visited[1] = 1;
	int count = 0;
	
	while (que.empty() == false)
	{
		int now = que.front();
		que.pop();
		if (now != lst[count])
		{
			cout << 0;
			exit(0);
		}
		for(int i=0;i<graph[now].size();i++)
		{
			int next = graph[now][i];
			if (visited[next] == 0)
			{
				visited[next] = 1;
				que.push(next);
			}
		}
		count++;
	}
	
	cout << 1;
}
