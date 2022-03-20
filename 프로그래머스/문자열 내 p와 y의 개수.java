class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toLowerCase();
        
        int p_cnt = 0;
        int y_cnt = 0;
        
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == 'p') {
                p_cnt += 1;
            }
            if (s.charAt(i) == 'y') {
                y_cnt += 1;
            } 
        }
        if (p_cnt == y_cnt) {
            answer = true;
        }
        else {
            answer = false;
        }

        return answer;
    }
}