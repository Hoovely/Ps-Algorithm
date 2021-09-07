#include <iostream>
using namespace std;

int n;
long long fibo[91];

int main()
{
	scanf("%d", &n);
	fibo[1] = 1;
	for(int i=2;i<n+1;i++)
	{
		fibo[i] = fibo[i-1] + fibo[i-2];
	}
	printf("%lld", fibo[n]);
}
