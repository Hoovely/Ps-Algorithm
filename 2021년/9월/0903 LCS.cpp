#include <iostream>
#include <cstring>
using namespace std;

string a,b;
int lcs[1001][1001];

int main()
{
	cin >> a >> b;
	for(int i=1;i<a.length()+1;i++)
	{
		for(int j=1;j<b.length()+1;j++)
		{
			if(a[i-1]==b[j-1])
			{
				lcs[i][j] = lcs[i-1][j-1] + 1;
			}
			else
			{
				lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j]);
				
			}
		}
	}
	
	cout << lcs[-1][-1];
}
