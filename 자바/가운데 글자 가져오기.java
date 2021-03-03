class Solution {
    public String solution(String s) {
        String answer = "";
        int s_count = s.length();
        
        if(s_count % 2 != 0) {
            answer += s.charAt((s_count)/2);
        }
        else {
            answer += s.charAt((s_count)/2-1);
            answer += s.charAt((s_count)/2);
        }
        return answer;
    }
}