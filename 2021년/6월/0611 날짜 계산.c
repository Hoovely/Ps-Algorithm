#include <stdio.h>

int main()
{
	int e,s,m,a=0,b=0,c=0,i=0;
	scanf("%d %d %d", &e,&s,&m);
	while(1)
	{
		i++;
		a++;
		b++;
		c++;
		if (a==16 || b==29 || c==20)
		{
			if (a==16) a = 1;
			if (b==29) b = 1;
			if (c==20) c = 1;
		}
		
		if (a==e & b==s & c==m) break;

	}
	
	printf("%d",i);
}
