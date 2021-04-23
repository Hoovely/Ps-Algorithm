// 백준_11050_이항계수_수학_브론즈 1 

#include <stdio.h>

int factorial(int num)
{
	if (num == 0 || num == 1) return 1;
	else return num*factorial(num-1);
}

int c(int n, int k)
{
	return factorial(n)/(factorial(n-k)*factorial(k));
}

int main()
{
	int n,k;
	scanf("%d %d", &n, &k);
	printf("%d", c(n,k));
}
