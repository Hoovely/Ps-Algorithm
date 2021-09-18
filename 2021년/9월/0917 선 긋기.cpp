#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<pair<int,int> > line;
const int INF = 2147483647;

int main()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		int x,y;
		scanf("%d %d",&x, &y);
		line.push_back(make_pair(x,y));
	}
	sort(line.begin(), line.end());
	
	int length = 0;
	int l = -INF;
	int r = -INF;
	for(int i=0;i<n;i++)
	{
		if(r < line[i].first)
		{
			length += r-l;
			l = line[i].first;
			r = line[i].second;
		}
		else r = max(r, line[i].second);
	}
	
	length += r-l;
	printf("%d", length);
}

