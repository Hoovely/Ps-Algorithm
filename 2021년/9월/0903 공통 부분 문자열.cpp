#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

string a,b;
int lcs[4001][4001];
int result = 0;

int main()
{
	cin >> a >> b;
	
	for(int i=1;i<a.length()+1;i++)
	{
		for(int j=1;j<b.length()+1;j++)
		{
			if(a[i-1] == b[j-1])
			{
				lcs[i][j] = lcs[i-1][j-1] + 1;
				result = max(result, lcs[i][j]);
			}
		}
	}
	
	cout << result;
}

