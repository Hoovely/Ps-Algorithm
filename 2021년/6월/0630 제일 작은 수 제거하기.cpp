// 프로그래머스_제일 작은 수 제거하기_수학_레벨 1

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