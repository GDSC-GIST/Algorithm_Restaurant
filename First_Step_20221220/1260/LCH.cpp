#include <cstdio>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

stack<int> s;
queue<int> q;
vector<int> v[1001];

bool visited[1001];

int main(){
	int n, m, start, x, y;
	scanf("%d %d %d", &n, &m, &start);
	for(int i=0; i<m; i++){
		scanf("%d %d", &x, &y);
		v[x].push_back(y);
		v[y].push_back(x);
	}
	
	s.push(start);
	while(!s.empty()){
		int temp = s.top();
		s.pop();
		if(!visited[temp]){
			visited[temp] = true;
			printf("%d ", temp);
			sort(v[temp].begin(), v[temp].end(), greater<int>());
			for(int i=0; i<v[temp].size(); i++)
				s.push(v[temp][i]);
		}
	}
	
	printf("\n");
	for(int i=1; i<=n; i++)
		visited[i] = false;
		
	q.push(start);
	while(!q.empty()){
		int temp = q.front();
		q.pop();
		if(!visited[temp]){
			visited[temp] = true;
			printf("%d ", temp);
			sort(v[temp].begin(), v[temp].end());
			for(int i=0; i<v[temp].size(); i++)
				q.push(v[temp][i]);
		}
	}
}
