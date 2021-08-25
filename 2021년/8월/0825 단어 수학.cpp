#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int n;
int alphabet[26];
vector<string> lst;

bool cmp(int a, int b)
{
	if (a>b) return true;
	return false;
}

int main()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		string str;
		cin >> str;
		lst.push_back(str);
	}
	
	for(int i=0;i<n;i++)
	{
		int j = 0;
		string S = lst[i];
		for(int k=S.length()-1;k>=0;k--)
		{
			alphabet[int(S[k]-'A')] += pow(10, j);
			j++;
		}
	}
	
	sort(alphabet, alphabet+26, cmp);
	
	int result = 0;
	for(int i=9;i>=0;i--)
	{
		result += i*alphabet[9-i];
	}
	
	cout << result;
	
	
	
}
