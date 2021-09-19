#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
vector<pair<int, int> > line;

int main()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		int x,y;
		scanf("%d %d", &x,&y);
		line.push_back(make_pair(x,y));
	}
	sort(line.begin(), line.end());
	
	int result = 0;
	int l = -2147483647;
	int r = -2147483647;
	for(int i=0;i<n;i++)
	{
		if(line[i].first > r)
		{
			result += r-l;
			l = line[i].first;
			r = line[i].second;
		}
		else r = max(r, line[i].second);
	}
	result += r-l;
	
	printf("%d", result);
}
