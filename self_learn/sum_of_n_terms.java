
import java.util.Scanner;

class SumOfNTerms{
    public int mySum(int n){
        if (n<=0){
            return 0;
        }
        return mySum(n-1) + n;
    }
}

class Main{
    public static void main(String[]args){
        SumOfNTerms sn = new SumOfNTerms();
        Scanner sc = new Scanner(System.in);
        
        System.out.println("enter number of terms: ");
        System.out.println(sn.mySum(sc.nextInt()));
    }
}