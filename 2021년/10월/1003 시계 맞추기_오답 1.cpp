#include <iostream>
#include <algorithm>
using namespace std;

#define INF 987654321

int c, n;
int result;
int times[16];

char button[10][17] = {
    "1110000000000000",
    "0001000101010000",
    "0000100000100011",
    "1000111100000000",
    "0000001110101000",
    "1010000000000011",
    "0001000000000011",
    "0000110100000011",
    "0111110000000000",
    "0001110001000100"};

bool isFinish()
{
    for (int i = 0; i < 16; i++)
    {
        if (times[i] != 0)
            return false;
    }
    return true;
}

void dfs(int switch_idx, int cnt)
{
    if (isFinish())
    {
        result = min(result, cnt);
        return;
    }
    if (switch_idx > 9)
        return;

    for (int i = 0; i < 4; i++)
    {
        dfs(switch_idx + 1, cnt + i);
        for (int j = 0; j < 16; j++)
        {
            if (button[switch_idx][j] == '1')
            {
                times[j] = (times[j] + 1) % 4;
            }
        }
    }
}

void INPUT()
{
    cin >> c;
    while (c--)
    {
        for (int i = 0; i < 16; i++)
        {
            int temp;
            cin >> temp;
            if (temp == 12)
                times[i] = 0;
            else
                times[i] = temp / 3;
        }

        result = INF;
        dfs(0, 0);
        if (result == INF)
            printf("%d\n", -1);
        else
            printf("%d\n", result);
    }
}

int main()
{
    INPUT();
}
