#include <cstdio>

int main(){
	int n, m, t;
	int arr[301][301];
	scanf("%d %d", &n, &m);
	
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			scanf("%d", &arr[i][j]);
	
	scanf("%d", &t);
	
	for(int test=0; test<t; test++){
		int x1, y1, x2, y2, sum = 0;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		
		for(int i=x1-1; i<x2; i++)
			for(int j=y1-1; j<y2; j++)
				sum += arr[i][j];
		
		printf("%d\n", sum);
	}
}
