#include<iostream>
using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;
	int arr[10001];
	for (int i = 0; i < n; i++) cin >> arr[i];

	int sum = 0, low = 0, high = 0, count = 0;
	while (1)
	{
		if (sum >= m) sum -= arr[low++];
		else if (high == n) break;
		else sum += arr[high++];
		if (m == sum) count++;
	}

	cout << count;
}