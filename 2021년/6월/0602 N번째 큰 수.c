// 백준2693_N번째 큰 수_정렬_실버 5
// 버블정렬 사용

#include <stdio.h>

void sort(int *nums)
{
	int i,j,temp;
	for (i=0;i<10;i++)
	{
		for(j=0;j<9-i;j++)
		{
			if (nums[j] > nums[j+1])
			{
				temp = nums[j];
				nums[j] = nums[j+1];
				nums[j+1] = temp;
			}
		}
	}
}

int main()
{
	int t,i,j,nums[10];
	
	scanf("%d", &t);
	for(i=0;i<t;i++)
	{
		for(j=0;j<10;j++) scanf("%d", &nums[j]);
		sort(nums);
		printf("%d\n", nums[7]);
	}
	
}
