#include <iostream>
#include <cmath>
using namespace std;

int n,r,c;
int cnt = 0;

void Z(int m, int size)
{
	if (m == 1)
	{
		if(r == 0 and c == 1) cnt+=1;
		else if(r == 1 and c == 0) cnt+=2;
		else if(r == 1 and c == 1) cnt+=3;
		
		cout << cnt;
		return ;
	}
	else
	{
		if(r < size and c >= size)
		{
			c-=size;
			cnt += pow(4,m-1);
		}
		else if(r >= size and c < size)
		{
			r-=size;
			cnt += pow(4,m-1)*2;
		}
		else if(r >= size and c >= size)
		{
			r-=size;
			c-=size;
			cnt += pow(4,m-1)*3;
		}
	}
	Z(m-1, size/2);
}

int main()
{
	cin >> n >> r >> c;
	Z(n, pow(2, n-1));
}
