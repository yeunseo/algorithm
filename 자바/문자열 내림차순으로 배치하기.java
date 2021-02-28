import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";

        // string을 char 배열로 변환
        char[] char_arr = s.toCharArray();
        // 배열 정렬(오름차순)
        Arrays.sort(char_arr);
        // 오름차순으로 정렬된 char배열을 뒤집어 내림차순으로 바꾸고 string으로 변환
        answer = new StringBuilder(new String(char_arr)).reverse().toString();
        return answer;
    }
}