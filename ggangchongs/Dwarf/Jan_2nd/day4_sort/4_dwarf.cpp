#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (auto command : commands)
    {
        int i = command.front();
        int k = command.back();
        command.pop_back();
        int j = command.back();
        vector<int> candidate(array.begin()+i-1, array.begin()+j);
        sort(candidate.begin(), candidate.end());
        answer.push_back(candidate[k-1]);
    }
    
    return answer;
}
