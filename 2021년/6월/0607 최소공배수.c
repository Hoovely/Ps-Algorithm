#include <stdio.h>

int main()
{
	int t,a,b,i,min,gcm = 1;
	scanf("%d",&t);
	while(t)
	{
		t--;
		scanf("%d %d",&a,&b);
		
		if (a>b) min = b;
		else min = a;
		
		for(i=min;i>0;i--)
		{
			if(a%i==0 && b%i == 0)
			{
				gcm = i;
				break;
			}
		}
		
		printf("%d\n",a*b/gcm);
		
	}	
}
