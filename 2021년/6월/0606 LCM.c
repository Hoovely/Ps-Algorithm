#include <stdio.h>

int main()
{
	int i,min,a,b,t,gcm = 1;
	scanf("%d",&t);
	while(t)
	{
		t--;
		scanf("%d %d", &a,&b);
		if (a>b) min = b;
		else min = a;
		
		for(i=min;i>0;i--)
		{
			if (a%i == 0 && b%i == 0) 
			{
				gcm = i;
				break;
			}
		}
		
		printf("%d\n",a/gcm*b/gcm*gcm);
	}
	
}
