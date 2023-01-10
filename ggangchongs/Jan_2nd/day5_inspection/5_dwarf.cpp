#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int row = 0, col = 0;
    for(auto size: sizes){
        int fir = max(size[0], size[1]);
        int sec = min(size[0], size[1]);
        if(fir > row){
            row = fir;
        }
        if(sec > col){
            col = sec;
        }
    }
    return row * col;
}
