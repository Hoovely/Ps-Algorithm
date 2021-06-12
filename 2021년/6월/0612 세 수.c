#include <stdio.h>
#include <stdlib.h>

int main()
{
	int nums[3],i,j;
	scanf("%d %d %d",&nums[0], &nums[1], &nums[2]);
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<2-i;j++)
		{
			if(nums[j] > nums[j+1])
			{
				int temp = nums[j+1];
				nums[j+1] = nums[j];
				nums[j] = temp;
			}
		}
	}
	
	printf("%d",nums[1]);
	
}
