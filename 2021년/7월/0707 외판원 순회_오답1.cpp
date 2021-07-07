// 백준_10971_외판원 순회 2_백트래킹_실버 2
// 오답 1 

#include <iostream>

using namespace std;

int n, visited[10],urban[10][10];
int result = 1561561846;

void solve(int first, int last, int sum, int cnt)
{
	if (cnt == n && first == last)
	{
		if (result >sum) result = sum;
		return;
	}
	
	for (int i=0;i<n;i++)
	{
		if (urban[last][i] == 0 || visited[last] == 1) continue;
		
		if (urban[last][i] != 0 && visited[last] == 0)
		{
			sum += urban[last][i];
			visited[last] = 1;
			
			if (result > sum) solve(first, i, sum, cnt+1);
			
			visited[last] = 0;
			sum -= urban[last][i];
		}
	}
}

int main()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++) cin >> urban[i][j];
	}
	
	for(int i=0;i<n;i++) solve(i,i,0,0);
	
	cout << result;
}
