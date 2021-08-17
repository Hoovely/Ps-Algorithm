#include <iostream>
#include <algorithm>
using namespace std;

int k,n;
long long ran_lst[10000];
long long max_cm = 0;

void binary_search(long long start, long long end)
{
	if(start>end) return;
	
	long long mid = (start+end)/2;

	if(mid == 0)
	{
		printf("%d",1);
		exit(0);	
	} 
	
	int m=0;
	for(int i=0;i<k;i++)
	{
		m += ran_lst[i]/mid;
	}
	
//	if(m==n)
//	{
//		printf("%d",mid);
//		exit(0);
//	}
	if(m>=n)
	{
		if(max_cm<mid) max_cm = mid;
		return binary_search(mid+1, end);
	}
	if(m<n) return binary_search(start, mid-1);
	
}
int main()
{
	scanf("%d %d", &k, &n);
	for(int i=0;i<k;i++) scanf("%d", &ran_lst[i]);
	binary_search(0, *max_element(ran_lst, ran_lst + k));
	printf("%d",max_cm);
}
