// 백준_9663_N-Queen_백트래킹_골드 5

#include <iostream>
using namespace std;

int n, queen = 0, y[14], p[27], m[27]; 

void dfs(int depth)
{
	if(depth == n)
	{
		queen++;
		return;
	}
	for(int i=0;i<n;i++)
	{
		if(y[i] == 0 and p[depth+i] == 0 and m[depth-i+n-1] == 0)
		{
			y[i] = p[depth+i] = m[depth-i+n-1] = 1;
			dfs(depth+1);
			y[i] = p[depth+i] = m[depth-i+n-1] = 0;
		}
	}
	
}

int main()
{
	cin >> n;
	dfs(0);
	cout << queen;
}
