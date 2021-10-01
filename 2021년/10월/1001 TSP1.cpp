#include <iostream>
#include <algorithm>
using namespace std;

int c,n;
double INF = 231561651;
double result;
double urban[8][8];
bool visited[8];

void dfs(int start_city, int now_city, double sum_cost, int cnt)
{
	if(cnt == n-1)
	{
		result = min(result,sum_cost);
		return;
	}
	
	for(int next_city=0;next_city<n;next_city++)
	{
		if(urban[now_city][next_city] == 0) continue;
		if(!visited[next_city])
		{
			double now_cost = urban[now_city][next_city];
			if(result > now_cost + sum_cost)
			{
				visited[next_city] = true;
				dfs(start_city, next_city, now_cost + sum_cost, cnt+1);
				visited[next_city] = false;
			}
		}
	}
}

void INPUT()
{
	cin >> c;
	while(c--)
	{
		cin >> n;
		visited[8] = {false,};
		for(int i=0;i<n;i++)
		{	
			for(int j=0;j<n;j++) cin >> urban[i][j];
		}
			
		result = INF;
		for(int i=0;i<n;i++)
		{
			visited[i] = true;
			dfs(i,i,0,0);
			visited[i] = false;
		}
		
		printf("%.10f\n", result);
	}
}

int main()
{
	INPUT();
}
