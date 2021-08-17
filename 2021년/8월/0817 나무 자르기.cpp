#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,m;
int forest[1000000];
int result = 0;

void binary_search(int start, int end)
{
	if(start>end) return;
	
	int mid = (start+end)/2;
	
	long long h = 0;
	for(int i=0;i<n;i++)
	{
		if(forest[i]-mid > 0) h += forest[i] - mid;
	}
	
	if (h==m)
	{
		printf("%d",mid);
		exit(0);
	}
	
	if (h>m)
	{
		if (mid > result) result = mid;
		binary_search(mid+1, end);
		return;
	}
	
	if (h<m)
	{
		binary_search(start, mid-1);
		return ;
	}
}

int main()
{
	scanf("%d %d", &n, &m);
	for(int i=0;i<n;i++) scanf("%d", &forest[i]);
	binary_search(0, *max_element(forest, forest+n));
	printf("%d",result);
}
