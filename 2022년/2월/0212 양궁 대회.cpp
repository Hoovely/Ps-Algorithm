#include <string>
#include <vector>

using namespace std;

int maxDiff;
vector<int> answer(1,-1);

bool isBetter(vector<int> lion)
{
	for(int i=10;i>=0;i--)
	{
		if(lion[i] > answer[i]) return false; // isBetter�� false�̸� ���� lion�� �������� �� ���ٴ� ���̴�.
		if(lion[i] < answer[i]) return true; // isBetter�� true�̸� ���� answer�� �������� �� ���ٴ� ���̴�.
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
        // ���� ū �������̷� ��� �� �� �ִ� ����� �������� �� ���   
		if(maxDiff == diff and isBetter(lion)) return;
		maxDiff = diff;
		answer = lion;	
	} 
}

void dfs(int idx, int arrows, vector<int> lion, vector<int> apeach)
{
	if(idx == 11 or arrows==0) // ���� ��� 
	{
		lion[10] += arrows; // ���� ȭ���� 0�� ���ῡ ���
		score(lion, apeach);
		lion[10] -= arrows;
		return; 
	}
	
	if(apeach[idx] < arrows) // 10-idx ������ ȭ���� ��� 
	{
		lion[idx] += apeach[idx]+1;
		dfs(idx+1, arrows-apeach[idx]-1, lion, apeach);
		lion[idx] -= apeach[idx]+1;	
	}	
	
	dfs(idx+1, arrows, lion, apeach); // ȭ���� �Ƚ�� �ѱ�� 
}

vector<int> solution(int n, vector<int> info) {
    vector<int> lion(11,0);
    dfs(0,n,lion,info);
    return answer;
}
