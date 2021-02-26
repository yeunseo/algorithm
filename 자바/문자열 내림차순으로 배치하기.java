import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        char[] char_arr = s.toCharArray();
        Arrays.sort(char_arr);
        answer = new StringBuilder(new String(char_arr)).reverse().toString();
        return answer;
    }
}