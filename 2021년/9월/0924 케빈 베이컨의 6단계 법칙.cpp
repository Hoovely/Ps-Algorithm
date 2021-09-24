#include <iostream>
#include <algorithm>
using namespace std;

int n,m;
int friends[100][100];
int INF = 1000000;

int main()
{
	scanf("%d %d", &n, &m);
	
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++) friends[i][j] = INF;
	}
	
	for(int i=0;i<m;i++)
	{
		int x,y; 
		scanf("%d %d",&x, &y);
		friends[x-1][y-1] = 1;
		friends[y-1][x-1] = 1;
	}
	
	for(int k=0;k<n;k++)
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++) friends[i][j] = min(friends[i][j], friends[i][k]+friends[k][j]);
		}
	}
	
	int min_num = INF;
	int result;
	for(int i=0;i<n;i++)
	{
		int kevin = 0;
		for(int j=0;j<n;j++)
		{
			if(friends[i][j] == INF)
			{
				kevin = INF;
				break;
			}
			else
			{
				kevin += friends[i][j];
			}
		}
		if(min_num > kevin)
		{
			min_num = kevin;
			result = i+1;
		}
	}
	
	printf("%d",result);
}
