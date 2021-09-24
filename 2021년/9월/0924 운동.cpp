#include <iostream>
#include <algorithm>
using namespace std;

int v,e;
int city[400][400];
int INF = 1000000000;

int main()
{
	scanf("%d %d", &v, &e);
	
	for(int i=0;i<v;i++)
	{
		for(int j=0;j<v;j++) city[i][j] = INF;
	}
	
	for(int i=0;i<e;i++)
	{
		int a,b,c;
		scanf("%d %d %d", &a, &b, &c);
		city[a-1][b-1] = c;
	}
	
	for(int k=0;k<v;k++)
	{
		for(int i=0;i<v;i++)
		{
			for(int j=0;j<v;j++) city[i][j] = min(city[i][j], city[i][k]+city[k][j]);
		}
	}
	
	int result = INF;
	for(int i=0;i<v;i++)
	{
		if(city[i][i] == INF) continue;
		else result = min(result, city[i][i]);
	}
	
	if(result == INF) printf("%d",-1);
	else printf("%d", result);
}
