#include <iostream>
using namespace std;

int c,n,m;
bool isFriends[10][10];
bool couple[10];
int result;

void SOLUTION()
{
	int start_idx = -1;
	for(int i=0;i<n;i++)
	{
		if(!couple[i])
		{
			start_idx = i;
			break;
		}
	}
	if(start_idx == -1)
	{
		result++;
		return;
	}

	for(int i=start_idx+1;i<n;i++)
	{
		if(!couple[i] and isFriends[start_idx][i])
		{
			couple[i] = couple[start_idx] = true;
			SOLUTION();
			couple[i] = couple[start_idx] = false;
		}
	}
}

void INPUT()
{
	scanf("%d", &c);
	while(c--)
	{
		scanf("%d %d", &n, &m);
		
		for(int i=0;i<n;i++)
		{
			couple[i] = false;
			for(int j=0;j<n;j++) isFriends[i][j] = false;
		}
		
		for(int i=0;i<m;i++)
		{
			int x,y;
			scanf("%d %d", &x, &y);
			isFriends[x][y] = true;
			isFriends[y][x] = true;
		}
		
		result = 0;
		SOLUTION();
		printf("%d\n", result);
	}
}

int main()
{
	INPUT();
}
