// 프로그래머스_정수 제곱근 판별_수학_레벨 1

#include<cmath>

long long solution(long long n) {
    
    double num = sqrt(n);
    
    if (num == int(num)) return (num + 1) * (num + 1);
    else return -1;

}
