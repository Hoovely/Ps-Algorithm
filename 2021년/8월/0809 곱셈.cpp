#include <iostream>
using namespace std;

long long a, b, c, half;

long long powpow(long long x, long long y)
{
	if (y == 1)	 return x;
	else if (y % 2 == 1) return powpow(x,y-1)*x;
	else if (y % 2 == 0)
	{
		half = powpow(x,y/2) % c;
		return half*half%c;
	}
}

int main()
{
	cin >> a >> b >> c;
	
	if (b == 0) cout << 1;
	else cout << powpow(a,b)%c;
}
