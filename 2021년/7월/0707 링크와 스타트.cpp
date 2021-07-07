// 백준_15661_링크와 스타트_백트래킹_실버 1

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int n, result = 123456456;
int lst[20][20];
vector<int>start;
vector<int>link;

void dfs(int index)
{
	if (index == n)
	{
		if (start.size() >= 2 && link.size() >= 2)
		{
			int sum_start = 0;
			int sum_link = 0;
			
			for (int i = 0;i<start.size();i++)
			{
				for(int j = i+1;j<start.size();j++)
				{
					sum_start += lst[start[i]][start[j]] + lst[start[j]][start[i]];
				}
			}
			
			for (int i = 0;i<link.size();i++)
			{
				for(int j = i+1;j<link.size();j++)
				{
					sum_link += lst[link[i]][link[j]] + lst[link[j]][link[i]];
				}
			}
			
			result = min(result, abs(sum_start-sum_link));
			
		}
		
		
		return;
	}
	
	start.push_back(index);
	dfs(index+1);
	start.pop_back();
	
	link.push_back(index);
	dfs(index+1);
	link.pop_back();
}



int main()
{
	cin >> n;
	
	for (int i = 0;i<n;i++)
	{
		for(int j = 0;j<n;j++) cin >> lst[i][j];
	}
	
	dfs(0);
	
	cout << result;
}
