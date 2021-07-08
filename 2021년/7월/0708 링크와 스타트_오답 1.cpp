// ����_15661_��ũ�� ��ŸƮ_��Ʈ��ŷ_�ǹ� 1
// ���� 1

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int n, team[20][20], result = 48498454165;
vector<int> start;
vector<int> link;

void solve(int index)
{
	if (index == n)
	{
		if (start.size() >= 2 && link.size() >= 2)
		{
			int start_sum = 0;
			int link_sum = 0;
			
			for (int i=0;i<start.size();i++)
			{
				for (int j=i+1;j<start.size();j++)
				{
					start_sum += team[start[i]][start[j]] + team[start[j]][start[i]];
				}
			}
			
			for (int i=0;i<link.size();i++)
			{
				for (int j=i+1;j<link.size();j++)
				{
					link_sum += team[link[i]][link[j]] + team[link[j]][link[i]];
				}
			}
			
			result = min(result, abs(start_sum-link_sum));
			
		}
		
		return ;
	}
	
	start.push_back(index);
	solve(index + 1);
	start.pop_back();
	
	link.push_back(index);
	solve(index + 1);
	link.pop_back();

}



int main()
{
	cin >> n;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++) cin >> team[i][j];
	}
	
	solve(0);
	
	cout << result;
}
