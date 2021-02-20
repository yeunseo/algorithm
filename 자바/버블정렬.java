/*  버블정렬
*   정렬 대상의 n번째 인덱스와 n+1번째 인덱스를 비교하여 큰 값을 뒤로 보내는 방법
*   첫 번째 과정이 처리되면 배열에서 가장 큰 수는 배열의 마지막에 위치하게 된다
*   그러므로 그 다음 탐색부터는 마지막요소는 비교할 필요 없다! => 내부 for문은 arr.length-i-1까지만 탐색
 */
for(int i = 0; i < arr.length; i++) {
    for(int j = 0 ; j < arr.length - i - 1 ; j++) {
        if(arr[j] > arr[j+1]) {
            int temp = arr[j+1];
            arr[j+1] = arr[j];
            arr[j] = temp;
        }
    }
}