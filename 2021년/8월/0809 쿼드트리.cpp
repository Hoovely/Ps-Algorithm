#include <iostream>
#include <string>
using namespace std;

string maps[64];

void solution(int m, int x, int y)
{
	char color = maps[x][y];
	for(int i=x;i<x+m;i++)
	{
		for(int j=y;j<y+m;j++)
		{
			if(color != maps[i][j])
			{
				cout << '(';
				solution(m/2, x, y);
				solution(m/2, x, y+m/2);
				solution(m/2, x+m/2, y);
				solution(m/2, x+m/2, y+m/2);
				cout << ')';
				return;
			}
		}
	}
	
	if(color == '0') cout << '0';
	else cout << '1';
}

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++) cin >> maps[i];
	
	solution(n, 0, 0);
}
