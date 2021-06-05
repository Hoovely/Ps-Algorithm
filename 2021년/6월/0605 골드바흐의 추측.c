#include <stdio.h>

int main()
{
	int i,j,k,t,n;
	int nums[10001] = {0,};
	for(i=2;i<10001;i++)
	{
		if (nums[i]) continue;
		for(j=2*i;j<10001;j+=i) nums[j] = 1;
	}
	
	scanf("%d", &t);
	while(t)
	{
		t--;
		scanf("%d", &n);
		
		for(i=n/2;i>1;i--)
		{
			if(nums[i] == 0 && nums[n-i] == 0) 
			{
				printf("%d %d\n", i,n-i);
				break;
			}
		}	
	}
	
}
