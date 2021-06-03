#include <stdio.h>

int main()
{
	int n,i,j, num, result[10001] = {0,};
	scanf("%d", &n);
	
	for(i=1;i<n+1;i++) 
	{
		scanf("%d", &num);
		result[num]++;
	}
	
	for(i=1;i<10001;i++)
	{
		for(j=0;j<result[i];j++) printf("%d\n", i);
	}
}
