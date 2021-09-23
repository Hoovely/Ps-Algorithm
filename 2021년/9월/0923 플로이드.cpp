#include <iostream>
#include <algorithm>
using namespace std;

int n,m;
int dist[101][101];
int INF = 10000001;
int main()
{
	scanf("%d", &n);
	scanf("%d", &m);
	
	for(int i=1;i<n+1;i++)
	{
		for(int j=1;j<n+1;j++)
		{
			if (i==j) dist[i][j] = 0;
			else dist[i][j] = INF; 
		}
	}
	
	for(int i=0;i<m;i++)
	{
		int a,b,c;
		scanf("%d %d %d",&a, &b, &c);
		dist[a][b] = min(dist[a][b], c);
	}
	
	for(int k=1;k<n+1;k++)
	{
		for(int i=1;i<n+1;i++)
		{
			for(int j=1;j<n+1;j++)
			{
				dist[i][j] = min(dist[i][j], dist[k][j]+dist[i][k]);
			}
		}
	}
	
	for(int i=1;i<n+1;i++)
	{
		for(int j=1;j<n+1;j++)
		{
			if(dist[i][j] == INF) printf("%d ", 0);
			else printf("%d ", dist[i][j]);
		}
		printf("\n");
	}
}
