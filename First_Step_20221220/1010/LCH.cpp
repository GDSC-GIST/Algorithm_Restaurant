#include <cstdio>

int main(){
	int comb[31][31];
	
	for(int i=0; i<31; i++){
		comb[1][i] = 0;
		comb[i][1] = i;
	}
	
	for(int i=2; i<30; i++)
		for(int j=2; j<30; j++){
			if(i < j) comb[i][j] = 0;
			else if (i == j) comb[i][j] = 1;
			else comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
		}
	
	int t;
	scanf("%d", &t);
	for(int test=0; test<t; test++){
		int n, m;
		scanf("%d %d", &n, &m);
		printf("%d\n", comb[m][n]);
	}
}
