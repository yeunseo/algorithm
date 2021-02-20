for(int a = 0 ; a < 5 ; a++){
    // 공백        
    for(int b = 0 ; b < 4-a ; b++){    
        System.out.print(" ");
    }
    // 별
    for(int b = 0 ; b < 2*a+1 ; b++){
        System.out.print("*");
    }
    // 줄바꿈
    System.out.println("");
}