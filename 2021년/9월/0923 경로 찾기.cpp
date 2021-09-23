#include <iostream>
#include <algorithm>
using namespace std;

int n;
int graph[100][100];
int INF = 1000000;

int main()
{
	scanf("%d", &n);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			int x;
			scanf("%d", &x);
			if(x==0) graph[i][j] = INF;
			else graph[i][j] = x;
		}
	}
	
	for(int k=0;k<n;k++)
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				graph[i][j] = min(graph[i][j], graph[k][j]+graph[i][k]);
			}
		}
	}
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(graph[i][j] == INF) printf("%d ", 0);
			else printf("%d ", 1);
		} 
		printf("\n");
	}
}
