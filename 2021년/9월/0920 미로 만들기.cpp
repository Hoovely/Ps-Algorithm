#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int n;
int MIN_NUM = 2147483647;
int graph[50][50];
int visited[100][50][50];

int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

struct moved
{
	int a;
	int b;
	int c;
};

int bfs()
{
	queue<moved> q;
	q.push({0,0,0});
	while(!q.empty())
	{
		int a = q.front().a;
		int b = q.front().b;
		int c = q.front().c;
		q.pop();
		
		if(a >= n+n-1) continue;
		
		if(a >= MIN_NUM) continue;
		
		if(b==n-1 and c==n-1) MIN_NUM = min(MIN_NUM, a);
		
		for(int i=0;i<4;i++)
		{
			int x = b + dx[i];
			int y = c + dy[i];
			if(0<=x and x<n and 0<=y and y<n)
			{
				if(graph[x][y] == 1)
				{
					if(visited[a][x][y] == 0)
					{
						visited[a][x][y] = visited[a][b][c] + 1;
						q.push({a,x,y});
					}
				}
				else
				{
					if(visited[a+1][x][y] == 0)
					{
						visited[a+1][x][y] = visited[a][b][c] + 1;
						q.push({a+1,x,y});
					}
				}
			}
		}	
	}
	
	return MIN_NUM; 
}

int main()
{
	scanf("%d", &n);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++) scanf("%1d", &graph[i][j]);
	}
	
	printf("%d", bfs());
}

