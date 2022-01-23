#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while(t--)
	{
		vector<int> arch[1001];
		int n, k, result[1001] = {0}, times[1001] = {0}, indegree[1001] = {0};
		cin >> n >> k;
		for(int i=1;i<n+1;i++) cin >> times[i];
		
		int x,y;
		for(int i=1;i<k+1;i++)
		{
			cin >> x >> y;
			indegree[y]++;
			arch[x].push_back(y);
		}
		
		queue<int> q;
		for(int i=1;i<n+1;i++)
		{
			if(indegree[i] == 0) 
			{
				q.push(i); 
				result[i] = times[i];
			}
		}
		
		while(!q.empty())
		{
			int now = q.front();
			q.pop();
			
			for(int next : arch[now])
			{
				if(--indegree[next] == 0) q.push(next);
				result[next] = max(result[next], result[now] + times[next]);
			}
		}
		
		int w;
		cin >> w;
		cout << result[w] << endl;
	}
}
