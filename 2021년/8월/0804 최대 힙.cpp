#include <iostream>
#include <queue>
using namespace std;

int n,x;
priority_queue<int> heap;

int main()
{
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d",&x);
		if(x==0)
		{
			if(heap.empty())
			{
				printf("%d\n",0);
			}
			else
			{
				printf("%d\n",heap.top());
				heap.pop();	
			}
		}
		else
		{
			heap.push(x);
		}
	}
} 
