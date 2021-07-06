// 백준_1759_암호 만들기_백트래킹_골드 5

#include <iostream>
#include <algorithm>

using namespace std;

int l,c;
char arr[15],result[15];

void solve(int index, int depth, int cnt1, int cnt2)
{
	if (depth == l && cnt1 >= 1 && cnt2 >= 2)
	{
		for (int i=0;i<l;i++) cout << result[i];
		cout << endl;
		return;
	}
	
	for (int i=index;i<c;i++)
	{
		result[depth] = arr[i];
		if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u')
		{
			solve(i+1,depth+1,cnt1+1,cnt2);
		}
		else
		{
			solve(i+1,depth+1,cnt1,cnt2+1);
		}
	}
}

int main()
{
	cin >> l >> c;
	for (int i=0;i<c;i++) cin >> arr[i];
	sort(arr, arr+c);
	solve(0,0,0,0);	
}
