#include <stdio.h>

int main()
{
	int i, count = 0;
	char str[101];
	scanf("%s", &str);
	for(i=0;str[i] != '\0';i++)
	{
		if(str[i] == 'a'|| str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') count++;
	}

	printf("%d", count);
}
