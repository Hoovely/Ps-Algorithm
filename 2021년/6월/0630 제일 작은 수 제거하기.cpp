// ���α׷��ӽ�_���� ���� �� �����ϱ�_����_���� 1

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    if (arr.size() == 1) return { -1 };
    else
    {
        int min_index = min_element(arr.begin(), arr.end()) - arr.begin();
        arr.erase(arr.begin() + min_index);
        return arr;
    }
}