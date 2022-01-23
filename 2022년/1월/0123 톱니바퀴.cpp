#include <iostream>
#include <deque>
#include <string>
#include <math.h>
using namespace std;

deque<char> dq[4];

void CurlDeque(int a, int d)
{
	char temp;
	if(d == 1)
	{
		for(int i=0;i<7;i++)
		{
			temp = dq[a][0];
			dq[a].pop_front();
			dq[a].push_back(temp);
		}
	}
	else
	{
		for(int i=0;i<7;i++)
		{
			temp = dq[a][7];
			dq[a].pop_back();
			dq[a].push_front(temp);
		}
	}
	
}

void Start(int a, int b)
{
	int flag[2][4] = {0};
	flag[0][a] = 1;
	flag[1][a] = b;
	int temp = b;
	for(int i=a-1;i>=0;i--)
	{
		if(dq[i][2] != dq[i+1][6])
		{
			temp *= -1;
			flag[0][i] = 1;
			flag[1][i] = temp;
		}
		else break;
	}
	temp = b;
	for(int i=a;i<3;i++)
	{
		if(dq[i][2] != dq[i+1][6])
		{
			temp *= -1;
			flag[0][i+1] = 1;
			flag[1][i+1] = temp;
		}
		else break;
	}
	for(int i=0;i<4;i++)
	{
		if(flag[0][i] == 1) CurlDeque(i, flag[1][i]);
	}
}

int main()
{
	string st;
	for(int i=0;i<4;i++)
	{
		cin >> st;
		for(int j=0;j<st.size();j++)
		{
			dq[i].push_back(st[j]);
		}
	}
	
	
	int k;
	cin >> k;
	for(int i=0;i<k;i++)
	{
		int a,b;
		cin >> a >> b;
		Start(a-1,b);
	}
	
	int score;
	for(int i=0;i<4;i++)
	{
		if(dq[i][0] == '1') score += pow(2,i);
	}
	
	cout << score;
}
