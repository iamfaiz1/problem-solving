public class Fibonacci {
    public static int myFib(int n){
        if(n<=0) return 0;

        if(n==1) return 1;

        return myFib(n-1) + myFib(n-2);
    }
    public static void main(String[] args) {
        System.out.println(Fibonacci.myFib(6));
    }
}


