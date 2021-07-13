// 백준_16929_Two Dots_DFS_골드 4
// 오답 1 

#include <iostream>
#include <cstring>
using namespace std;

int n, m, start_x, start_y;
int dx[4] = {1,-1,0,0}, dy[4] = {0,0,1,-1};
int visited[50][50];
char graph[50][50];

void dfs(int now_x, int now_y, int cnt)
{
	if (cnt >= 4)
	{
		for(int i=0;i<4;i++)
		{
			if(start_x == now_x + dx[i] and start_y == now_y + dy[i])
			{
				cout << "Yes";
				exit(0);
			} 
		}
	}
	
	for(int i=0;i<4;i++)
	{
		int next_x = now_x + dx[i];
		int next_y = now_y + dy[i];
		if(0<=next_x<n and 0<=next_y<m and visited[next_x][next_y] == 0 and graph[next_x][next_y] == graph[start_x][start_y])
		{
			visited[next_x][next_y] = 1;
			dfs(next_x, next_y, cnt+1);
		}
	}
}


int main()
{
	cin >> n >> m;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++) cin >> graph[i][j];
	}
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			memset(visited,0,sizeof(visited));
			
			start_x = i;
			start_y = j;
			
			visited[i][j] = 1;
			dfs(i,j,1);		
		}
	}
	
	cout << "No";
}
