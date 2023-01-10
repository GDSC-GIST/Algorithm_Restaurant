#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int prev = -1;

    for(auto candidate : arr){
        if(prev != candidate){
            answer.push_back(candidate);
        }
        prev = candidate;
    }

    return answer;
}
