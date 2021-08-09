#include <iostream>
using namespace std;

int maps[2187][2187];
int mi = 0, ze = 0, on = 0;

void paper(int m, int x, int y)
{
	int number = maps[x][y];
	for(int i=x;i<m+x;i++)
	{
		for(int j=y;j<m+y;j++)
		{
			if(number != maps[i][j])
			{
				for(int k=0;k<3;k++)
				{
					paper(m/3, x+m/3*k, y);
					paper(m/3, x+m/3*k, y+m/3);
					paper(m/3, x+m/3*k, y+m/3*2);
				}
				return;
			}
		}
	}
	if(number == -1) mi++;
	else if(number == 0) ze++;
	else on++;
}

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++) cin >> maps[i][j];
	}
	
	paper(n, 0, 0);
	
	cout << mi << endl << ze << endl << on;
}
