#include <iostream>
using namespace std;

int n, S[20];

void go(int idx, int cur_sum, int *lst)
{
	if(n==idx)
	{
		lst[cur_sum] = 1;
		return;
	}
	
	go(idx+1, cur_sum, lst);
	go(idx+1, cur_sum + S[idx], lst);
}

int main()
{
	cin >> n;
	int max_num = 100000*n+1;
	int lst[max_num] = {0,};
	for(int i=0;i<n;i++) cin >> S[i];
	go(0,0,lst);
	
	for(int i=1;i<max_num;i++)
	{
		if(lst[i]==0)
		{
			cout << i;
			break;
		}
	}
}
