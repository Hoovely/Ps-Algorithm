#include <iostream>
#include <vector>

using namespace std;

int a,b,flag = 0;
vector<int> visited;
vector<int>N[2000];

void dfs(int index, int count)
{
	if(count == 4)
	{
		flag = 1;
		return;
	}
	
	for(int i=0;i<a;i++)
	{
		if(N[index][i] == 1 and visited[i] == 0) 
		{
			visited[i] = 1;
			dfs(i,count+1);
			visited[i] = 0;
		}
	}
}

int main()
{
	int x,y;
	cin >> a >> b;
	
	for(int i=0;i<b;i++)
	{
		cin >> x >> y;
		N[x].push_back(y);
		N[y].push_back(x);
	}
	
	for(int i=0;i<a;i++)
	{
		visited[i] = 1;
		dfs(i,0);
		visited[i] = 0;
		
		if(flag == 1) break;
	}
	
	cout << flag;
	
}
