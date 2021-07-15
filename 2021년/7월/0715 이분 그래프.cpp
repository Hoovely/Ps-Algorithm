// 백준_1707_이분 그래프_DFS_골드 4

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int k, v, e, flag, check[20001],visited[20001];
vector<int> graph[20001];

void input_color(int now)
{
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		
		if(check[next] == 0)
		{
			if(check[now] == 1) check[next] = 2;
			else check[next] = 1;
			
			input_color(next);
		}
	}
}

void solution(int now)
{
	for(int i=0;i<graph[now].size();i++)
	{
		int next = graph[now][i];
		if(check[next] == check[now]) 
		{
			flag = 1;
			return ;
		}
		
		if(visited[next] == 0)
		{
			visited[next] = 1;
			solution(next);
		}
		
		if (flag == 1) return;
	}
}

int main()
{
	cin >> k;
	while(k--)
	{
		cin >> v >> e;
		
		for(int i=1;i<v+1;i++)
		{
			graph[i].resize(0);
			check[i] = 0;
			visited[i] = 0;
		}
		
		for(int i=0;i<e;i++)
		{
			int x,y;
			cin >> x >> y;
			graph[x].push_back(y);
			graph[y].push_back(x);	
		}
		
		for(int i=1;i<v+1;i++)
		{
			if(check[i] == 0)
			{
				check[i] = 1;
				input_color(i);
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
		
		if(flag == 1) cout << "NO" << "\n";
		else cout << "YES" << "\n";
	}	
} 
