import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        ArrayList<Integer> array = new ArrayList<Integer>();
        
        for(int i: arr) {
            if(i % divisor == 0) {
                array.add(i);
            }
        }
        // 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환
        if(array.size() == 0) {
            array.add(-1);
        }

        // answer리스트의 크기를 arrayList와 맞추기
        answer = new int[array.size()];

        // answer리스트에 arrayList값 넣기
        for(int j = 0; j<answer.length; j++) {
            answer[j] = array.get(j);
        }
        // 오름차순으로 정렬
        Arrays.sort(answer);
        
        return answer;
    }
}