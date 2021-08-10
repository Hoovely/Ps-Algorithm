#include <iostream>
using namespace std;

int n, maps[128][128];
int blue = 0, white = 0;

void paper(int m, int x, int y)
{
	int color = maps[x][y];
	for(int i=x;i<x+m;i++)
	{
		for(int j=y;j<y+m;j++)
		{
			if(maps[i][j] != color)
			{
				paper(m/2, x, y);
				paper(m/2, x, y+m/2);
				paper(m/2, x+m/2, y);
				paper(m/2, x+m/2, y+m/2);
				return;
			}
		}
	}
	
	if(color == 0) white++;
	else blue++;
}

int main()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++) cin >> maps[i][j];
	}
	
	paper(n,0,0);
	
	cout << white << endl << blue;
}
