#include <iostream>

using namespace std;

int n,m,visited[50][50];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
char graph[50][50];

void print()
{
	cout << "Yes";
	exit(0);
}

void dfs(int x, int y, int first_x, int first_y, int cnt)
{
	if (cnt >= 4)
	{
		for(int i=0;i<4;i++)
		{
			if(first_x == x + dx[i] and first_y == y + dy[i]) print();
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
			if(visited[i][j] == 0)
			{
				visited[i][j] = 1;
				dfs(i,j,i,j,0);
			}
		}
	}
	
}
