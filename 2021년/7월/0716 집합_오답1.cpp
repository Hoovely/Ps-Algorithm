// 백준_11723_집합_비트마스킹_실버 5 
// 오답 1
 
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int n,x,s[21];
	char cmd[10];
	scanf("%d", &n);
	while(n--)
	{
		scanf("%s", cmd);
		
		if(cmd[1] == 'd')
		{
			scanf("%d",&x);
			s[x] = 1;
		}
		else if(cmd[0] == 'r')
		{
			scanf("%d",&x);
			s[x] = 0;
		}
		else if(cmd[0] == 'c')
		{
			scanf("%d",&x);
			if(s[x] == 1) printf("%d\n",1);
			else printf("%d\n",0);
		}
		else if(cmd[0] == 't')
		{
			scanf("%d",&x);
			if(s[x] == 1) s[x] = 0;
			else s[x] = 1;
		}
		else if(cmd[1] == 'l')
		{
			fill(s+1,s+21,1);
		}
		else if(cmd[0] == 'e')
		{
			fill(s+1,s+21,0);
		}
	}
}
