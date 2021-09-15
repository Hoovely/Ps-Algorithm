#include <iostream>
using namespace std;

int c, n, l;
int cost[1001];
double MIN_NUM = 2147484.0;

void SOLUTION()
{
	double result = MIN_NUM;
	for(int i=1;i<=n-l+1;i++)
	{
		int day = 1;
		int sum_num = 0;
		for(int j=i;j<=n;j++)
		{
			sum_num += cost[j];
			if(day>=l)
			{
				double aver_num =  (1.0)*sum_num/day;
				if(aver_num<result) result = aver_num;
			}
			day++;
		}
	}
	
	printf("%.12f\n", result);
}

void INPUT()
{
	scanf("%d", &c);
	while(c--)
	{
		scanf("%d %d", &n, &l);
		for(int i=1;i<=n;i++) scanf("%d", &cost[i]);
		SOLUTION();
	}
}

int main()
{
	INPUT();
}
