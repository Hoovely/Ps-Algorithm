#include <string>
#include <vector>

using namespace std;

int maxDiff;
vector<int> answer(1,-1);

bool isBetter(vector<int> lion)
{
	for(int i=10;i>=0;i--)
	{
		if(lion[i] > answer[i]) return false; // isBetter이 false이면 현재 lion의 과녁판이 더 좋다는 뜻이다.
		if(lion[i] < answer[i]) return true; // isBetter이 true이면 현재 answer의 과녁판이 더 좋다는 뜻이다.
	}
}

void score(vector<int>& lion, vector<int> apeach)
{
	int lionScore = 0, apeachScore = 0;
	for(int i=0;i<11;i++)
	{
		if(lion[i] > apeach[i]) lionScore += 10-i;
		if(apeach[i] > 0 and apeach[i] >= lion[i]) apeachScore += 10-i;
	}
	
	int diff = lionScore - apeachScore;
	if(diff > 0 and diff>=maxDiff)
	{
        // 가장 큰 점수차이로 우승 할 수 있는 방법이 여러가지 일 경우   
		if(maxDiff == diff and isBetter(lion)) return;
		maxDiff = diff;
		answer = lion;	
	} 
}

void dfs(int idx, int arrows, vector<int> lion, vector<int> apeach)
{
	if(idx == 11 or arrows==0) // 점수 계산 
	{
		lion[10] += arrows; // 남은 화살을 0점 과녁에 쏜다
		score(lion, apeach);
		lion[10] -= arrows;
		return; 
	}
	
	if(apeach[idx] < arrows) // 10-idx 점수에 화살을 쏜다 
	{
		lion[idx] += apeach[idx]+1;
		dfs(idx+1, arrows-apeach[idx]-1, lion, apeach);
		lion[idx] -= apeach[idx]+1;	
	}	
	
	dfs(idx+1, arrows, lion, apeach); // 화살을 안쏘고 넘긴다 
}

vector<int> solution(int n, vector<int> info) {
    vector<int> lion(11,0);
    dfs(0,n,lion,info);
    return answer;
}
