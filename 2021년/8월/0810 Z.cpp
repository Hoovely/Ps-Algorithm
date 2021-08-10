#include <iostream>
#include <cmath>
using namespace std;

int n,r,c,cnt = 0;

void Z(int size)
{
	if (n==1)
	{
		if(r == 0 and c == 0) cout << cnt;
		else if(r == 0 and c == 1) cout << cnt+1;
		else if(r == 1 and c == 0) cout << cnt+2;
		else if(r == 1 and c == 1) cout << cnt+3;
		return;
	}
	else
	{
		if(r < size and c >= size)
		{
			c -= size;
			cnt += pow(4, n-1);
		}
		else if(r >= size and c < size)
		{
			r -= size;
			cnt += pow(4, n-1)*2;
		} 
		else if(r >= size and c >= size)
		{
			r -= size;
			c -= size;
			cnt += pow(4, n-1)*3;
		}
		n--;
		Z(size/2);
	}
}

int main()
{
	 cin >> n >> r >> c;
	 Z(pow(2,n-1));
}
