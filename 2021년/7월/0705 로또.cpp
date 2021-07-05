// 백준_6603_로또_백트래킹_실버 2

#include <iostream>
#include <vector>

using namespace std;

int k;
int nums[13];
int result[6];

void solve(int index, int depth)
{
	if (depth == 6)
	{
		for(int i =0;i<6;i++) cout << result[i] << ' ';
		cout << endl;
		return;
	}
	
	
	for(int i=index;i<k;i++)
	{
		result[depth] = nums[i];
		solve(i+1, depth+1);
	}
}

int main()
{
	while(1)
	{
		cin >> k;
		if (k == 0) break;
		for (int i = 0;i<k;i++) cin >> nums[i];
		solve(0,0);
		cout << endl;
	}
	
}
