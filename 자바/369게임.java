 /*
         * 369 게임 (박수 몇 번?)
*/
        
        //실행 횟수
        int count = 100;
 
        //chkNum 실행 값의 시작
        for(int chkNum = 1 ;chkNum <= count;chkNum++) {
            
            //문자열로 형변환
            String strCnt = String.valueOf(chkNum);
            System.out.print(strCnt);

            for(int j=0;j <strCnt.length();j++) {
                char chk = strCnt.charAt(j);
                if(chk == '3' || chk == '6' || chk == '9') {
                    System.out.print("짝");
                }
            }
            //줄바꿈
            System.out.println();
        }