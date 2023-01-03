#include <stdio.h>

int main()
{
	int i,temp,ans=0,min=101;
	for(i=0;i<7;i++)
	{
		scanf("%d",&temp);
		if(temp%2 == 1) ans+=temp;
		if(temp%2 == 1 && temp < min) min = temp;
	}
	if(ans != 0) printf("%d\n%d",ans,min);
	else printf("-1");
}
