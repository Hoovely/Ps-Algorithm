#include <iostream>
#include <queue>
using namespace std;

int n,x;
priority_queue<int,vector<int>,greater<int> > heap;

int main()
{
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&x);
		if(x==0)
		{
			if(heap.size() == 0)
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
