#include <cstdio>

int main(){
	int n, x, dp[11] = {0, 1, 2, 4};
	scanf("%d", &n);
	for(int i=4; i<11; i++){
		dp[i] += dp[i-1] + dp[i-2] + dp[i-3];
	}
	
	for(int i=0; i<n; i++){
		scanf("%d", &x);
		printf("%d\n", dp[x]);
	}
}
