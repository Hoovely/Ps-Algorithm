#include <iostream>
#include <vector>
using namespace std;

int c,h,w;
int result;
bool gamemap[31][20][20];

int dx[4][3] = {{0,1,1}, {0,1,0}, {0,1,1}, {0,0,1}};
int dy[4][3] = {{0,0,-1}, {0,0,1}, {0,0,1}, {0,1,1}};

void dfs()
{
	bool isFinish = true;
	int a,b;
	for(int i=0;i<h;i++)
	{
		for(int j=0;j<w;j++)
		{
			if(!gamemap[c][i][j])
			{
				isFinish = false;
				a = i;
				b = j;
				break;
			}
		}
		if(!isFinish) break; 
	}
	if(isFinish)
	{
		result++;
		return;
	}
	
	for(int i=0;i<4;i++)
	{
		bool isPossible = true;
		vector<pair<int, int> > possibleDirection;
		for(int j=0;j<3;j++)
		{
			int x = a + dx[i][j];
			int y = b + dy[i][j];
			if(x<0 or x>=h or y<0 or y>=w)
			{
				isPossible = false;
				break;
			}
			if(gamemap[c][x][y])
			{
				isPossible = false;
				break;
			}
			possibleDirection.push_back(make_pair(x,y));
		}
		if(isPossible)
		{
			for(int j=0;j<possibleDirection.size();j++)
			{
				int next_x = possibleDirection[j].first;
				int next_y = possibleDirection[j].second;
				gamemap[c][next_x][next_y] = true;
			}
			
			dfs();
			
			for(int j=0;j<possibleDirection.size();j++)
			{
				int next_x = possibleDirection[j].first;
				int next_y = possibleDirection[j].second;
				gamemap[c][next_x][next_y] = false;
			}
		}
	}		
}

void INPUT()
{
	scanf("%d", &c);
	while(c--)
	{
		scanf("%d %d", &h, &w);
		int white_count = 0;
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				char temp;
				scanf(" %c",&temp);
				if(temp == '#') gamemap[c][i][j] = true;
				else
				{
					gamemap[c][i][j] = false;
					white_count++;
				}
			}
		}
		if(white_count % 3 != 0)
		{
			printf("%d\n",0);
			continue;
		}
		
		result = 0;
		dfs();
		printf("%d\n", result);
	}
}

int main()
{
	INPUT();
}
