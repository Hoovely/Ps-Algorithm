// 백준_2747_피보나치 수_DP_브론즈 3

#include <stdio.h>

int nums[46];

int fibonacci(int n)
{
	if (n<=1) return n;
	else if (nums[n] != 0) return nums[n];
	else
	{
		nums[n] = fibonacci(n-1) + fibonacci(n-2);
		return nums[n];
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	printf("%d", fibonacci(n));
}
