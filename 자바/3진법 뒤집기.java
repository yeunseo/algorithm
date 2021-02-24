import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList<Integer> temp = new ArrayList<>();

        
        // 3진법으로 만들어 temp에 추가(역순으로 저장됨)
        while(true) {
            // 더 이상 나눌 값 없으면 끝냄
            if(n < 3) {
                temp.add(n);
                break;
            }
            // 나머지를 temp에 저장
            temp.add(n%3);
            // n값 갱신
            n /= 3;   
        }
        // 10진수로 표현
        for(int i = 0; i < temp.size(); i++) {
            answer += (temp.get(i) * (Math.pow(3, temp.size()-1-i)));
        }        
        return answer;
    }
}