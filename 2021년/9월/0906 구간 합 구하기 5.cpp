#include <iostream>
using namespace std;

int m,n;
int graph[1025][1025];
int dp[1025][1025];

int main()
{
	scanf("%d %d", &n, &m);
	for(int i=1;i<n+1;i++)
	{
		for(int j=1;j<n+1;j++) scanf("%d", &graph[i][j]);
	}
	
	for(int i=1;i<n+1;i++)
	{
		for(int j=1;j<n+1;j++)
		{
			dp[i][j] = graph[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
		}
	}
	
	for(int i=0;i<m;i++)
	{
		int x,y,xx,yy;
		scanf("%d %d %d %d", &x, &y, &xx, &yy);		
		printf("%d\n", dp[xx][yy] - dp[xx][y-1] - dp[x-1][yy] + dp[x-1][y-1]);
	}
}
