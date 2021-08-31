#include <iostream>
#include <queue>
using namespace std;

int n,m;
int graph[1000][1000], visited[2][1000][1000];
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

typedef struct Q
{
	int a;
	int b;
	int c;	
}Q;

queue<Q>moved;

int bfs()
{
	visited[0][0][0] = 1;
	moved.push({0,0,0});
	while(!moved.empty())
	{
		int x = moved.front().a;
		int y = moved.front().b;
		int z = moved.front().c;
		moved.pop();
		
		if(x == n-1 and y == m-1) return visited[z][x][y];
		
		for(int i=0;i<4;i++)
		{
			int x1 = x + dx[i];
			int y1 = y + dy[i];
			if(x1 >= 0 and y1 >= 0 and x1 < n and y1 < m and visited[z][x1][y1] == 0)
			{
				if(graph[x1][y1] == 0)
				{
					visited[z][x1][y1] = visited[z][x][y] + 1;
					moved.push({x1,y1,z});
				}
				else if(graph[x1][y1] == 1 and z == 0)
				{
					if(visited[1][x1][y1] == 0)
					{
						visited[1][x1][y1] = visited[0][x][y] + 1;
						moved.push({x1,y1,1});
					}
				}
				
			}
		}
	}
	return -1;
}

int main()
{
	cin >> n >> m;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++) scanf("%1d",&graph[i][j]);
	}
	
	cout << bfs() << endl;
}
