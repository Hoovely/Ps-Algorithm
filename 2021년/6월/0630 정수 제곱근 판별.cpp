// ���α׷��ӽ�_���� ������ �Ǻ�_����_���� 1

#include<cmath>

long long solution(long long n) {
    
    double num = sqrt(n);
    
    if (num == int(num)) return (num + 1) * (num + 1);
    else return -1;

}
