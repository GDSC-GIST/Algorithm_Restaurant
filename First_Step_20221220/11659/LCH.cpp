#include <cstdio>

int a[100001];

int main(){
    int n, q;
    scanf("%d %d", &n, &q);
    
    for(int i=1; i<=n; i++)
        scanf("%d", &a[i]);
    
    for(int i=2; i<=n; i++)
        a[i] += a[i-1];
    
    for(int i=0; i<q; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        printf("%d\n", a[y] - a[x-1]);
    }
}
