#include <iostream>
using namespace std;

int n,h;
int down[500001], up[500001];

int main()
{
	cin >> n >> h;
	for(int i=1;i<n+1;i++)
	{
		int obstacle;
		cin >> obstacle;
		if(i%2==0) up[obstacle]++;
		else down[obstacle]++;
	}
	
	for(int i=h-1;i>0;i--)
	{
		down[i] += down[i+1];
		up[i] += up[i+1];
	}
	
	int Min_Obstacle = n;
	int Count = 0;
	for(int i=1;i<h+1;i++)
	{
		if(Min_Obstacle > down[i] + up[h-i+1])
		{
			Min_Obstacle = down[i] + up[h-i+1];
			Count = 1;
		}
		else if(Min_Obstacle == down[i] + up[h-i+1]) Count++;
	}
	
	cout << Min_Obstacle << ' ' << Count;
}
