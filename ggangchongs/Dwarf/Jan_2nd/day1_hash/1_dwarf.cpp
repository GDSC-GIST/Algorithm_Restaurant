#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    for(auto iter = completion.rbegin(); iter != completion.rend(); ++iter)
    {
        if(participant.back() != *iter)
        {
            answer = participant.back();
            break;
        }
        participant.pop_back();
    }
    if(answer.empty())      answer = participant[0];
    return answer;
}
