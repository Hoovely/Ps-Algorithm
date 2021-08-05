#include <iostream>
#include <queue>
#include <vector>
#include <algorithm> 
using namespace std;

int INF = 1000000000;
int n, m, start, last;
int dist[1001];
int route[1001];
vector<pair<int, int> > graph[1001];
vector<int> route_v;
priority_queue<pair<int, int> > heap;

int main()
{
	scanf("%d %d",&n,&m);
	while(m--)
	{
		int a,b,c;
		scanf("%d %d %d",&a,&b,&c);
		graph[a].push_back(make_pair(b,c));
	}
	scanf("%d %d",&start,&last);
	
	fill(dist, dist+n+1, INF);
	dist[start] = 0;
	
	heap.push(make_pair(0, start));
	while(!heap.empty())
	{
		int now_cost = -heap.top().first;
		int now_urban = heap.top().second;
		heap.pop();
		
		if (dist[now_urban] < now_cost) continue;
		
		for(int i=0;i<graph[now_urban].size();i++)
		{
			int next_urban = graph[now_urban][i].first;
			int next_cost = graph[now_urban][i].second;
			if(dist[next_urban] > now_cost + next_cost)
			{
				route[next_urban] = now_urban;
				dist[next_urban] = now_cost + next_cost;
				heap.push(make_pair(-dist[next_urban], next_urban));
			} 
		}
	}
	
	int temp = last;
	while(temp)
	{
		route_v.push_back(temp);
		temp = route[temp];
	}
	
	printf("%d\n", dist[last]);
	printf("%d\n", route_v.size());
	for(int i=route_v.size()-1;i>=0;i--)
	{
		printf("%d ",route_v[i]);	
	}	
}
