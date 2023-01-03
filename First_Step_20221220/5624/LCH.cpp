#include <cstdio>

int arr[5001], check[400001];

int main(){
	int n, ans = 0;
	scanf("%d", &n);
	for(int i=0; i<n; i++)
		scanf("%d", &arr[i]);
	// x + y + z = k  =>  x + y = k - z
	for(int k = 0; k < n; k++){
		for(int z = 0; z < k; z++){
			if(check[arr[k] - arr[z] + 200000]){
				ans++;
				break;
			}
		}
		
		for(int x = 0; x <= k; x++)
			check[arr[x] + arr[k] + 200000] = 1;
	}
	printf("%d", ans);
}
