#include <stdio.h>

int main()
{
	int n,i,j,num[246913] = {0,};
	
	for(i=1;i<246913;i++)
	{
		if (i==1) 
		{
			num[1] = 1;
			continue;
		}
		
		for(j=2*i;j<246913;j += i) num[j] = 1;
	}

	while(1)
	{
		int count=0;
		scanf("%d", &n);
		if (n==0) break;
		
		for(i=n+1;i<=2*n;i++)
		{
			if(num[i] == 0) count++; 
		}
		
		printf("%d\n",count);
		
	}
}
