#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int v,e,k;
int INF_num = 100000000000;
int dist[20001];
vector<pair<int,int> > graph[20001];
priority_queue<pair<int,int> > heap;
 
int main()
{
	scanf("%d %d %d",&v, &e, &k);
	fill(dist, dist+v+1, INF_num);
	dist[k] = 0;
	while(e--)
	{
		int a,b,c;
		scanf("%d %d %d",&a, &b, &c);
		graph[a].push_back(make_pair(b,c));
	}
	
	heap.push(make_pair(0, k));
	while(!heap.empty())
	{
		int now_d = -heap.top().first;
		int now_v = heap.top().second;
		heap.pop();
			
		if(dist[now_v] < now_d) continue;
		
		for(int i=0;i<graph[now_v].size();i++)
		{
			int next_v = graph[now_v][i].first;
			int next_d = now_d + graph[now_v][i].second;
			if(dist[next_v] > next_d)
			{
				dist[next_v] = next_d;
				heap.push(make_pair(-next_d, next_v));
			}
		}
	}
	
	for(int i=1;i<v+1;i++)
	{
		if(dist[i] == INF_num) printf("INF\n");
		else printf("%d\n",dist[i]);
	}
}
